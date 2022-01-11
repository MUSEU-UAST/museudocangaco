from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone

from portal.models.global_choices import USERS


class Post(models.Model):
    CATEGORIES = (
        ("N", "Notícia"),
        ("P", "Página"),
    )

    STATUS = (
        ("0", "Rascunho"),
        ("1", "Publicar")
    )

    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    slug = models.SlugField(unique=True)

    cover = models.ImageField(blank=True, null=True)
    category = models.CharField(max_length=255, choices=CATEGORIES)
    content = RichTextUploadingField(config_name="default")
    status = models.CharField(max_length=255, choices=STATUS)
    author = models.CharField(max_length=255, choices=USERS)

    publication_date = models.DateTimeField(default=timezone.now)

    @classmethod
    def get_news(cls):
        return Post.objects.filter(category="N")

    @classmethod
    def get_recent(cls):
        return Post.get_news().order_by("-publication_date")

    def get_cover(self):
        if self.cover:
            return self.cover.url
        else:
            return None
