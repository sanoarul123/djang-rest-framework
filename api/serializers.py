from rest_framework import serializers
from students.models import student
from employees.models import Employee


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'