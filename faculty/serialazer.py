from rest_framework.serializers import ModelSerializer
from .models import *


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class ChairSerializer(ModelSerializer):
    teachers = TeacherSerializer(many=True, required=False)

    class Meta:
        model = Chair
        fields = '__all__'


class EmployeeSerializer(ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class FacultySerializer(ModelSerializer):
    # employees = EmployeeSerializer(many=True, required=False)

    class Meta:
        model = Faculty
        fields = '__all__'
