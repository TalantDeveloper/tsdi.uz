from django.contrib import admin
from .models import Chair, Teacher, Faculty, Employee, ChairsShip
from modeltranslation.admin import TranslationAdmin


@admin.register(Chair)  # Register is the Kafedralar
class ChairAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'sub_name']
    list_display_links = ['id', 'name', 'sub_name']
    list_filter = ['name', 'sub_name']
    search_fields = ['id', 'name', 'sub_name']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Teacher)
class TeacherAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'chair', 'position', 'is_head', 'number']
    list_display_links = ['id', 'name', 'chair', 'position']
    list_filter = ['chair', 'is_head']
    search_fields = ['id', 'name', 'number']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Faculty)
class FacultyAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'sub_name']
    list_display_links = ['id', 'name', 'sub_name']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name', 'sub_name']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Employee)
class EmployeeAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'fakultet', 'position', 'is_dean', 'number']
    list_display_links = ['id', 'name', 'fakultet']
    list_filter = ['id', 'fakultet', 'is_dean']
    search_fields = ['id', 'name', 'fakultet']

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
