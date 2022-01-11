from django.db import models


class Event(models.Model):
    STATUS = (
        ("0", "Ativo"),
        ("1", "Inativo")
    )

    title = models.CharField(max_length=255)
    cover = models.ImageField(max_length=255)
    slug = models.SlugField(unique=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    address = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255, choices=STATUS, default=0)

    def get_period(self):
        return f"De {self.start_date.strftime('%d/%m/%y às %H:%H')} até {self.end_date}"
