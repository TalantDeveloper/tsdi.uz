from django.shortcuts import render
from .models import Chair, Teacher, Faculty, Employee
from .serialazer import TeacherSerializer, ChairSerializer, FacultySerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


def faculties_view(request):
    faculties = Faculty.objects.all()
    data = FacultySerializer(faculties, many=True).data

    return JsonResponse(data, safe=False)
