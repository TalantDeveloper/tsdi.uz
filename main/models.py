from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Position(models.Model):
    name = models.CharField(max_length=255, verbose_name='Lavozimi')  # Translation
    sub_name = models.CharField(max_length=255, verbose_name='sub name')

    def __str__(self):
        return self.name


class Rectory(models.Model):  # Rektor va Direktorlar
    """Rector and Directors of Institute"""
    name = models.CharField(max_length=255, verbose_name="F.I.SH")
    image = models.ImageField(upload_to="./rector/", verbose_name="Rasm")
    content = RichTextUploadingField(verbose_name="Haqida")  # Translation

    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    academic_title = models.TextField(verbose_name="Unvoni")  # Translation
    is_rector = models.BooleanField(default=False, verbose_name="Rektormi?")
    reception = RichTextUploadingField(verbose_name="Qabul vaqti")  # Translation

    number = models.CharField(max_length=50, verbose_name="Telefon nomer", null=True, blank=True)
    address = models.TextField(verbose_name="Manzil", null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    instagram = models.URLField(verbose_name="Instagram", null=True, blank=True)
    telegram = models.URLField(verbose_name="Telegram", null=True, blank=True)
    facebook = models.URLField(verbose_name="Facebook", null=True, blank=True)
    linkedin = models.URLField(verbose_name="Linkedin", null=True, blank=True)

    def __str__(self):
        return self.name


class Department(models.Model):  # Markaz va Bo'limlar
    """"""
    name = models.CharField(max_length=255, verbose_name="Markaz nomi")  # Translation
    content = RichTextUploadingField(verbose_name="Markaz haqida", null=True, blank=True)  # Translation

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=250, verbose_name="F.I.SH.")
    image = models.ImageField(upload_to="./markaz/", default="./markaz/avatar.jpg", verbose_name="Rasm")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Markaz")

    position = models.TextField(verbose_name="Lavozimi")  # Translation
    academic_title = models.TextField(verbose_name="Unvoni", null=True, blank=True)  # Translation
    is_chief = models.BooleanField(default=False, verbose_name="Boshliqmi:")

    number = models.CharField(max_length=50, verbose_name="Telefon nomer", null=True, blank=True)
    email = models.EmailField(max_length=50, verbose_name="Email", null=True, blank=True)

    def __str__(self):
        return self.name


