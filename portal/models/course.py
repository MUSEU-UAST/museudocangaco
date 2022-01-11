from django.db import models

from portal.models.global_choices import USERS


class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    cover = models.ImageField()
    date = models.DateField()
    author = models.CharField(max_length=255, choices=USERS)
    description = models.TextField()
