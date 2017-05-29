# from django.shortcuts import render

from django.http import HttpResponse

# from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view

from .models import Student, Bus
from .serializers import StudentSerializer

def index(request):
    return HttpResponse("<h1>YO! It's Pizza Time!!</h1>")

# class StudentList(APIView):
# 	def get(self, request):
# 		students = Student.objects.all()

# 		serializers = StudentSerializer(students, many=True) 

# 		return Response(serializers.data)

# class ListCreateStudents(generics.ListCreateAPIView):
# 	# def get(self, request):
# 	# 	students = Student.objects.all()

# 	# 	serializers = StudentSerializer(students, many=True) 

# 	# 	return Response(serializers.data)

# 	queryset = Student.objects.all()
# 	serializer_class = StudentSerializer


# @api_view(['GET'])
# def student_count(request):
#     """
#     Count students in a given bus
#     """
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)




@api_view(['GET', 'POST'])
def student_list(request):
    """
    List all queries of the table, or create a new query.
    """
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, student_id, bus_pk):
    """
    Get, udpate, or delete a specific query from the table
    """
    # return HttpResponse("WORKING")
    try:
    	# bus_fk = Bus.objects.get(bus_pk)
    	student = Student.objects.filter(bus=bus_pk, student_id=student_id)
    	# student = student_in_bus.objects.get(pk=pk)

    	# student = Student.objects.get(pk=pk)

    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)