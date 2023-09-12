from django.shortcuts import render
from .models import Chair, Teacher, Faculty, Employee
from .serialazer import TeacherSerializer, ChairSerializer, FacultySerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


@api_view(('GET', ))
def faculties_view(request):
    faculties = Faculty.objects.all()
    chairs = Chair.objects.all()
    faculties_serializer = FacultySerializer(faculties, many=True)
    chairs_serializer = ChairSerializer(chairs, many=True)
    combined_data = {
        'faculty_data': faculties_serializer.data,
        'chair_data': chairs_serializer.data,
    }
    return Response(combined_data)


@api_view(('GET', ))
def chairs_view(request):
    chairs = Chair.objects.all()
    chair_serializer = ChairSerializer(chairs, many=True)
    combined_data = {
        'chair_data': chair_serializer.data
    }
    return Response(combined_data)