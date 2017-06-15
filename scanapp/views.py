from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view

from .models import Student, Bus, User
from .serializers import StudentSerializer, BusSerializer, RegisterSerializer, UserSerializer#, PasswordChangeSerializer, EmailSerializer

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator

from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render
from .forms import RegisterForm,DeleteUserForm

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.utils.encoding import force_bytes

from django.contrib.auth.tokens import default_token_generator

import requests

# from twilio.rest import Client
# from django.conf import settings

from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView

from django.shortcuts import render_to_response, get_object_or_404

from django.template import Context, RequestContext

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

def student_detail(request, student_biometric_id, bus_route_number):
    """
    Get, udpate, or delete a specific query from the table
    """

    try:
    	bus_num = Bus.objects.filter(bus_route_number=bus_route_number)
    	bus_pk = bus_num[0].id
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





@method_decorator(csrf_exempt)
@api_view(['GET'])

def student_bus_detail(request, bus_id):

	"""
    Get, udpate, or delete a specific query from the table
    """

	try:
		bus = Bus.objects.filter(id=bus_id)
	except Bus.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		
		serializer = BusSerializer(bus,many=True)
		return Response(serializer.data)



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

# @method_decorator(csrf_exempt)
# @api_view(['GET', 'PUT', 'DELETE', 'POST'])

# def bus_detail(request, bus_pk):

# 	"""
#     Get, udpate, or delete a specific query from the table
#     """

# 	# try:
# 	# 	bus = Bus.objects.filter(id=bus_pk)
# 	# except Bus.DoesNotExist:
# 	# 	return Response(status=status.HTTP_404_NOT_FOUND)

# 	try:
# 		bus = Bus.objects.filter(id=bus_pk)
# 		# bus = bus.get(id=bus_pk)

# 	except Bus.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'GET':
# 		# bus = Bus.objects.filter(id=bus_pk)
# 		serializer = BusSerializer(bus,many=True)
# 		return Response(serializer.data)

# 	# if request.method == 'GET':
# 	# 	serializer = BusSerializer(bus,many=True)
# 	# 	return Response(serializer.data)

# 	elif request.method == 'PUT':
# 		serializer = BusSerializer(bus, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		else:
# 			return Response(
# 				serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	elif request.method == 'POST':
# 		serializer = BusSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		else:
# 			return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	elif request.method == 'DELETE':
# 		bus.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)



@method_decorator(csrf_exempt)
@api_view(['GET', 'PUT', 'DELETE', 'POST'])

def bus_app_detail(request, bus_route_number):

	"""
    Get, udpate, or delete a specific query from the table
    """

	try:
		bus = Bus.objects.get(bus_route_number=bus_route_number)
	except Bus.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		bus = Bus.objects.filter(bus_route_number=bus_route_number)
		serializer = BusSerializer(bus,many=True)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = BusSerializer(bus, data=request.data)

		if serializer.is_valid():
			# print(serializer.data)
			serializer.append(serializer.data)
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
@api_view(['GET'])
def email(request, admission_number, message):


	try:
		student = Student.objects.filter(admission_number=admission_number)

	except Student.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)


	if request.method == 'GET':
		
		# message = retrieve_message(message)
    	
		subject = "Student Admission Number " + str(student[0].admission_number) + " " + student[0].student_name + " Suggestion"
		from_email = settings.EMAIL_HOST_USER
		to_email = student[0].email_id
		contact_message = message

		send_mail(subject, 
			contact_message,
			from_email,
			to_email,
			fail_silently = False
			)
		return Response(status=status.HTTP_201_CREATED)

	else:
			return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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




def reset_password(request, username):

	associated_user = User.objects.filter(username=username) 
	# print(associated_user[0].username)

	if associated_user.exists():
		print("True")
		user = User.objects.filter(username=associated_user[0].username)
		student = Student.objects.filter(admission_number=associated_user[0].username)
		parent_number = student[0].phone_number
		print(parent_number)
		print(user)
		print(user[0])
		c = {
		'uid': urlsafe_base64_encode(force_bytes(user[0].pk)),
		'user': user,
		'token': default_token_generator.make_token(user[0]),
		'protocol': 'http',
		}

		print(c['token'])
		print(c['uid'])
		parent_number_str = str(parent_number)
		parent_number_str = parent_number_str.replace("+91","")
		# urls = 'http://127.0.0.1:8000/scanapp/send/' + parent_number_str + '/token/' + c['token'] + '/uid/' + c['uid']
		message_text = 'Click or copy paste the below link to change the password'
		message_url = 'https://biometric-app.herokuapp.com/scanapp/password/change?token=' + c['token'] + '&uid=' + str(c['uid']) + '/auth'
		# message_url = 'http://127.0.0.1:8000/scanapp/password/change?token=' + c['token'] + '&uid=' + str(c['uid']) + '/auth'
		message_regards1 = 'Regards,'
		message_regards2 = 'Team Manav Rachna'
		message = message_text + '\n\n\n' + message_url + '\n\n\n' + message_regards1 + '\n' + message_regards2
		# url = 'http://127.0.0.1:8000/scanapp/email/' + username + '/message/' + message_text
		# r = requests.get(url, params=request.GET)
		# print(r)




		subject = "Password Change Request - Student Admission Number " + str(student[0].admission_number) + " " + student[0].student_name
		from_email = settings.EMAIL_HOST_USER
		to_email = [student[0].email_id]
		contact_message = message

		send_mail(subject, 
			contact_message,
			from_email,
			to_email,
			fail_silently = False
			)

		return render(request, 'scanapp/email_sent.html')

	else:
		return render(request, 'scanapp/user_invalid.html')




def awesome_method(request, phone_number, message):
	phone_number = "+91" + str(phone_number)
	message = message
	from_ = '+17866296415'
	to = phone_number;
	client = Client(
    settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
	response = client.messages.create(
	    body=message, to=to, from_=from_)






def callback(request):
	token = request.GET.get('token')
	uid = request.GET.get('uid').replace("/auth","").replace("b'","").replace("'","")

	context = {
		'token' : token,
		'uid' : uid,
	}

	return render(request, 'scanapp/callback.html', context)






@method_decorator(csrf_exempt)
def delete_user(request):
    form = DeleteUserForm(request.POST or None)
    if form.is_valid():
        reg = form.save()
        # album.save()
        return render(request, 'scanapp/delete_user.html')
    context = {
        "form": form,
    }
    return render(request, 'scanapp/delete_user.html', context)




@method_decorator(csrf_exempt)
@api_view(['GET', 'POST'])

def delete_user_model(request):


    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
        	print("-------------------")
        	print(serializer['username'].value)
        	username=serializer['username'].value
        	User.objects.filter(username=username).delete()
        	return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
        	return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response({"detail": _("New password has been saved.")})





# class PasswordChangeView(GenericAPIView):
#     """
#     Calls Django Auth SetPasswordForm save method.

#     Accepts the following POST parameters: new_password1, new_password2
#     Returns the success/fail message.
#     """
#     serializer_class = PasswordChangeSerializer
#     # permission_classes = (IsAuthenticated,)

#     # @sensitive_post_parameters_m
#     def dispatch(self, *args, **kwargs):
#         return super(PasswordChangeView, self).dispatch(*args, **kwargs)

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"detail": _("New password has been saved.")})





# MSG91_AUTHKEY = '154618AwWLYscrj593050fe'
# MSG91_ROUTE = '4'

# # class Msg91SmsBackend(BaseSmsBackend):

#     def send_messages(self, messages):
#         for message in messages:
#             for to in message.to:
#                 values = {
#                           'authkey' : MSG91_AUTHKEY,
#                           'mobiles' : to,
#                           'message' : message.body,
#                           'sender' : message.from_phone,
#                           'route' : MSG91_ROUTE
#                           }
#                 print(values)
#                 url = "https://control.msg91.com/api/sendhttp.php" # API URL
#                 postdata = urllib.urlencode(values) # URL encoding the data here.
#                 req = urllib2.Request(url, postdata)
#                 response = urllib2.urlopen(req)
#                 output = response.read() # Get Response
#                 print(response)