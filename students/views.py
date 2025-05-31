from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def students(request):
    students = [
        {'id':24,'Name': "Md Sanoarul Islam",'Age':24}

    ]
    return HttpResponse(students)
