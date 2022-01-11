from django.db import models


class Book(models.Model):
    CATEGORIES = (
        ("L", "Livro"),
        ("C", "Cartilha")
    )

    title = models.CharField(verbose_name="título", max_length=255)
    category = models.CharField(verbose_name="categoria", max_length=255, choices=CATEGORIES, default=0)
    slug = models.SlugField(verbose_name="slug", unique=True)
    cover = models.ImageField(verbose_name="capa", upload_to="capas")
    authors = models.CharField(verbose_name="autoria", max_length=255)
    publisher = models.CharField(verbose_name="editora", max_length=255)
    release_year = models.IntegerField(verbose_name="ano de publicação")
    isbn = models.DecimalField(verbose_name="ISBN", max_digits=13, decimal_places=0)
    description = models.TextField(verbose_name="descrição")
