# Generated by Django 4.0.1 on 2022-01-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=96, verbose_name='título'),
        ),
    ]
