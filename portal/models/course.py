from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    cover = models.ImageField()
    date = models.DateField()
    # author = models.CharField(max_length=255, choices=USERS)
    author = models.CharField(max_length=255)
    description = models.TextField()
