from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view

from .models import Student, Bus, User
from .serializers import StudentSerializer, BusSerializer, EmailSerializer, RegisterSerializer

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator

from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render
from .forms import RegisterForm

#biometric-app/scanapp/
def index(request):
    return HttpResponse("<h1>YO! It's Pizza Time!!</h1>")



#biometric-app/scanapp/student_all
@method_decorator(csrf_exempt)
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



#biometric-app/scanapp/bus/bus_id/student/student_id

@method_decorator(csrf_exempt)
@api_view(['GET', 'PUT', 'DELETE', 'POST'])

def student_detail(request, student_biometric_id, bus_pk):
    """
    Get, udpate, or delete a specific query from the table
    """

    try:
    	student = Student.objects.filter(bus=bus_pk)
    	student = student.get(student_biometric_id=student_biometric_id)
    	
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
    	student = Student.objects.filter(bus=bus_pk, student_biometric_id=student_biometric_id)
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


    elif request.method == 'POST':
    	serializer = StudentSerializer(data=request.data)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data, status=status.HTTP_201_CREATED)
    	else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#biometric-app/scanapp/parent/admission_number
@method_decorator(csrf_exempt)
@api_view(['GET', 'PUT', 'DELETE', 'POST'])

def parent_view(request, admission_number):
    """
    Get, udpate, or delete a specific query from the table
    """

    try:
    	
    	student = Student.objects.filter(admission_number=admission_number)

    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
    	
    	serializer = StudentSerializer(student,many=True)
    	return Response(serializer.data)

    elif request.method == 'PUT':
    	student = Student.objects.get(admission_number=admission_number)
    	serializer = StudentSerializer(student, data=request.data)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data)
    	else:
    		return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'POST':
    	serializer = StudentSerializer(data=request.data)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data, status=status.HTTP_201_CREATED)
    	else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#biometric-app/scanapp/bus_all

@method_decorator(csrf_exempt)
@api_view(['GET', 'POST'])

def bus_list(request):
    """
    List all queries of the table, or create a new query.
    """
    if request.method == 'GET':
        buss = Bus.objects.all()
        serializer = BusSerializer(buss, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#biometric-app/scanapp/bus/bus_id

@method_decorator(csrf_exempt)
@api_view(['GET', 'PUT', 'DELETE', 'POST'])

def bus_detail(request, bus_pk):

	"""
    Get, udpate, or delete a specific query from the table
    """

	try:
		bus = Bus.objects.filter(id=bus_pk)
	except Bus.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = BusSerializer(bus,many=True)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = BusSerializer(bus, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(
				serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'POST':
		serializer = BusSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		bus.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)




#to post an email
# @api_view(['POST'])
# def email(request, admission_number, message):


# 	try:
# 		student = Student.objects.filter(admission_number=admission_number)

# 	except Student.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)


# 	if request.method == 'POST':
		
# 		message = retrieve_message(message)
    	
# 		subject = "Student Admission Number " + str(student[0].admission_number) + " " + student[0].student_name + " Suggestion"
# 		from_email = settings.EMAIL_HOST_USER
# 		to_email = [from_email, 'rishabhnarangcool@gmail.com']
# 		contact_message = message

# 		send_mail(subject, 
# 			contact_message,
# 			from_email,
# 			to_email,
# 			fail_silently = False
# 			)
# 		return Response(status=status.HTTP_201_CREATED)

# 	else:
# 			return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# def retrieve_message(message):
# 	message = message.replace("-n", "\n")
# 	message = message.replace("-", " ")

# 	return message







#student registration ie creating usernames and password of students in db
#biometric-app/scanapp/signup_student
@method_decorator(csrf_exempt)
def register_student(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        reg = form.save()
        # album.save()
        return render(request, 'scanapp/register_student.html')
    context = {
        "form": form,
    }
    return render(request, 'scanapp/register_student.html', context)




#bus registration ie creating usernames and password of buses in db
#biometric-app/scanapp/signup_student
@method_decorator(csrf_exempt)
def register_bus(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        reg = form.save()
        # album.save()
        return render(request, 'scanapp/register_bus.html')
    context = {
        "form": form,
    }
    return render(request, 'scanapp/register_bus.html', context)


