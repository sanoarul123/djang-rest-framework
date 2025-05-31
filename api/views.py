from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def studentView(request):
    students = {
        'id':24,
        'Name': "Md Sanoarul Islam",
        'Age':24
    }
    return JsonResponse(students)