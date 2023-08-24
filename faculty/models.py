from django.db import models


class Chair(models.Model):  # Kafedralar
    """Chairs models of Faculty at the Institute"""
    pass


class Teacher(models.Model):  # Kafedradagi Ustozlar
    """Teachers in Departments belonging to the Faculties of the Institute"""
    pass


class Faculty(models.Model):  # Fakultetlar
    """Faculties of the Institute"""
    pass


class Employee(models.Model):  # Fakultet xodimlari
    """Employees in Faculty at the Institute"""
    pass