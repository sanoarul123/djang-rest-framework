from students.models import  student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET','POST'])
def studentView(request):
    if request.method == 'GET':
        students = student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def studentDetailView(request, pk):
    try:
        student_instance = student.objects.get(pk=pk)  # Renamed variable
    except student.DoesNotExist:                       # Model class unchanged
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method== 'GET':
        serializer = StudentSerializer(student_instance)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student_instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        student_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

