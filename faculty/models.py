from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Chair(models.Model):  # Kafedralar
    """Chairs models of Faculty at the Institute"""
    name = models.CharField(max_length=255, verbose_name="Kafedra nomi")  # Translation
    sub_name = models.CharField(max_length=150, verbose_name="Sub nomi")
    content = RichTextUploadingField(null=True, blank=True, verbose_name='Kadedra haqida')  # Translation

    def __str__(self):
        return self.name


class Teacher(models.Model):  # Kafedradagi Ustozlar
    """Teachers in Departments belonging to the Faculties of the Institute"""
    name = models.CharField(max_length=150, verbose_name="F.I.SH.")
    image = models.ImageField(upload_to="./kafedra/", default="./kafedra/avatar.jpg", verbose_name="Rasm")
    chair = models.ForeignKey(Chair, on_delete=models.CASCADE, verbose_name="Kafedra")

    position = models.TextField(verbose_name="Ustoz haqida", null=True, blank=True)  # Translation
    academic_title = models.EmailField(verbose_name="Unvoni", null=True, blank=True)  # Translation

    number = models.CharField(max_length=50, verbose_name="Telefon nomer", null=True, blank=True)
    email = models.CharField(max_length=50, verbose_name="Email", null=True, blank=True)

    def __str__(self):
        return self.name


class Faculty(models.Model):  # Fakultetlar
    """Faculties of the Institute"""
    name = models.CharField(max_length=250, verbose_name="Fakultet nomi")  # Translation
    sub_name = models.CharField(max_length=250, verbose_name="fakultet_nomi")
    content = RichTextUploadingField(null=True, blank=True, verbose_name="Fakultet haqida")  # Translation
    chairs = models.ManyToManyField(Chair, verbose_name="Fafedralar", through='ChairsShip')


class ChairsShip(models.Model):  # Kefedralar va Fakultetlarni bog'lash klasi
    """"""
    chair = models.ForeignKey(Chair, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.faculty} - {self.chair}"


class Employee(models.Model):  # Fakultet xodimlari
    """Employees in Faculty at the Institute"""
    name = models.CharField(max_length=150, verbose_name="F.I.SH")
    image = models.ImageField(default="./fakultet/avatar.jpg", upload_to="./fakultet/", verbose_name='Rasm')
    fakultet = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    position = models.TextField(verbose_name="Lavozimi")  # Translation
    academic_title = models.TextField(verbose_name="Unvoni")  # Translation
    is_dean = models.BooleanField(default=False, verbose_name="Dekanmi?")

    number = models.CharField(max_length=50, verbose_name="Telefon nomer", null=True, blank=True)
    email = models.EmailField(max_length=50, verbose_name="Email", null=True, blank=True)

    def __str__(self):
        return self.name
