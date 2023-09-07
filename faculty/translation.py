from .models import Chair, Teacher, Faculty, Employee, Position
from modeltranslation.translator import TranslationOptions, register


@register(Chair)
class ChairTranslationOption(TranslationOptions):
    fields = ('name', 'content')


@register(Teacher)
class TeacherTranslationOption(TranslationOptions):
    fields = ('position', 'academic_title')


@register(Faculty)
class FacultyTranslationOption(TranslationOptions):
    fields = ('name', 'content')


@register(Position)
class PositionTranslationOption(TranslationOptions):
    fields = ('name',)


@register(Employee)
class EmployeeTranslationOption(TranslationOptions):
    fields = ('academic_title',)
