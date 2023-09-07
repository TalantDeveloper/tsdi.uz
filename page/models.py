from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=250, verbose_name="Name")  # Translation
    image = models.ImageField(upload_to="./partner/", verbose_name="Rasm")
    url = models.URLField(verbose_name="Link")

    def __str__(self):
        return self.name


class Category(models.Model):  # Kategoriya Pages
    """Category of Pages"""
    pass


class Page(models.Model):  # Pages
    """All Pages of Institute"""
    pass
