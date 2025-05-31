from django.shortcuts import render
from django.http import JsonResponse
from students.models import  student

# Create your views here.
def studentView(request):
    students = student.objects.all()
    students_list = list(students.values())
    return JsonResponse(students_list,safe=False)