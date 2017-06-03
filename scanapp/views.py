# from django.shortcuts import render

from django.http import HttpResponse

# from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view

from .models import Student, Bus, User
from .serializers import StudentSerializer, BusSerializer, EmailSerializer, RegisterSerializer
# from .permissions import IsOwnerOrReadOnly#, IsAuthenticated


from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator

from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render
from .forms import RegisterForm

# import json

# from twilio.rest import Client
# from django.conf import settings

# from sendsms.backends.base import BaseSmsBackend


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

# class StudentMixin(object):
# 	permission_classes = (IsOwnerOrReadOnly,)

# 	def pre_save(self, obj):
# 		obj.owner = self.request.user

#------------------------------------------------------------

@method_decorator(csrf_exempt)
@api_view(['GET', 'POST'])

def student_list(request):
    """
    List all queries of the table, or create a new query.
    """
    #permission_classes = (IsAuthenticated,) -- ++++++++++++++TODO+++++++++++++++++++
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

#------------------------------------------------------------


# class StudentView(APIView):
# 	permission_classes = (IsAuthenticated,)





#------------------------------------------------------------

@method_decorator(csrf_exempt)
@api_view(['GET', 'PUT', 'DELETE', 'POST'])

def student_detail(request, student_biometric_id, bus_pk):
    """
    Get, udpate, or delete a specific query from the table
    """
    # return HttpResponse("WORKING")


    try:
    	# student_in_bus = Bus.objects.filter(id=bus_pk)
    	student = Student.objects.filter(bus=bus_pk)
    	student = student.get(student_biometric_id=student_biometric_id)
    	# student = student_in_bus.objects.get(student_id=student_id)

    	# student = Student.objects.get(pk=pk)

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



@method_decorator(csrf_exempt)
@api_view(['GET', 'PUT', 'DELETE', 'POST'])

def parent_view(request, admission_number):
    """
    Get, udpate, or delete a specific query from the table
    """
    # return HttpResponse("WORKING")


    try:
    	# student_in_bus = Bus.objects.filter(id=bus_pk)
    	# student = Student.objects.filter(bus=bus_pk)
    	# student = Student.get(admission_number=admission_number)
    	# student = student_in_bus.objects.get(student_id=student_id)
    	student = Student.objects.filter(admission_number=admission_number)
   
    	# student = Student.objects.get(pk=pk)

    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
    	# student = Student.objects.filter(admission_number=admission_number)
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

@api_view(['POST'])
def email(request, admission_number, message):


	try:
		student = Student.objects.filter(admission_number=admission_number)

	except Student.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)


	if request.method == 'POST':
		# print(student[0].admission_number)
		# serializer = EmailSerializer(data=request.data)
		# if serializer.is_valid():
			# print("+++++++++++++++++++++++++")
			# # print(serializer)
			# check=request.POST
			# print(check.get('student_name'))
			# # print(request.POST.getlist('admission_number'))
			# print("+++++++++++++++++++++++++")
			# for i in serializer.data:
			# 	for j in i:
			# 		print(j)
			# return Response(serializer.data)

			# myDict = dict(serializer.iterlists())
			# print(serializer.dict())

			# print(dict(request.POST))

			# print(json.dumps(serializer))

		message = retrieve_message(message)
    	
		subject = "Student Admission Number " + str(student[0].admission_number) + " " + student[0].student_name + " Suggestion"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'rishabhnarangcool@gmail.com']
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



def retrieve_message(message):
	message = message.replace("-n", "\n")
	message = message.replace("-", " ")

	return message








# @method_decorator(csrf_exempt)
# def reg(request):
# 	return render(request, 'scanapp/reg.html')


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


# class RegistrationView(APIView): 
# 	permission_classes = () 
# 	def post(self, request):
# 		serializer = RegisterSerializer(data=request.data) 

# 		# Check format and unique constraint 
# 		if not serializer.is_valid(): 
# 			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
# 		data = serializer.data 
# 		u = User.objects.create(username=data['username']) 
# 		u.set_password(data['password']) 
# 		u.save() 

# 		# Create OAuth2 client 
# 		name = u.username 
# 		client = Client(user=u, name=name, url='' + name, client_id=name, client_secret='', client_type=1) 
# 		client.save() 
# 		return Response(serializer.data, status=status.HTTP_201_CREATED)


# class RegistrationView(APIView):
# 	def get post(self, request):
# 		serializer = RegisterSerializer(data=request.data)




#------------------------------------------------------------

# @api_view(['GET', 'POST'])
# def student_list(request):
#     """
#     List all queries of the table, or create a new query.
#     """
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StudentDetail(StudentMixin, ListCreateAPIView):
# 	@api_view(['GET', 'PUT', 'DELETE'])
# 	def student_detail(request, student_id, bus_pk):
#     	"""
#     	Get, udpate, or delete a specific query from the table
#     	"""
#     	# return HttpResponse("WORKING")
#     	try:
#     		# bus_fk = Bus.objects.get(bus_pk)
#     		student = Student.objects.filter(bus=bus_pk, student_id=student_id)
#     		# student = student_in_bus.objects.get(pk=pk)

#     		# student = Student.objects.get(pk=pk)

#     	except Student.DoesNotExist:
#         	return Response(status=status.HTTP_404_NOT_FOUND)

#     	if request.method == 'GET':
#         	serializer = StudentSerializer(student,many=True)
#         	return Response(serializer.data)

#     	elif request.method == 'PUT':
#         	serializer = StudentSerializer(student, data=request.data)
#         	if serializer.is_valid():
#             	serializer.save()
#             	return Response(serializer.data)
#         	else:
#             	return Response(
#                 	serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     	elif request.method == 'DELETE':
#         	student.delete()
#         	return Response(status=status.HTTP_204_NO_CONTENT)









# class StudentMixin(object):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     permission_classes = (IsOwnerOrReadOnly,)

#     def pre_save(self, obj):
#         obj.owner = self.request.user


# class StudentList(StudentMixin, ListCreateAPIView):
#     pass


# class StudentDetail(StudentMixin, RetrieveUpdateDestroyAPIView):
#     pass











# class CreateUserView(CreateAPIView):

#     model = get_user_model()
#     permission_classes = [
#         permissions.AllowAny # Or anon users can't register
#     ]
#     serializer_class = UserSerializer







# def awesome_method(request):
# 	message = 'YO'
# 	from_ = '+17866296415'
# 	to = '+919999688904';
# 	client = Client(
# 	    settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
# 	response = client.messages.create(
# 	    body=message, to=to, from_=from_)


# MSG91_AUTHKEY = '154618AwWLYscrj593050fe'
# MSG91_ROUTE = '4'

# class Msg91SmsBackend(BaseSmsBackend):

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