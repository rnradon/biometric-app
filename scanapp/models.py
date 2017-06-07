from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import Permission, User

# Create your models here.


class Bus(models.Model):
	driver_name = models.CharField(max_length=100)
	conductor_name = models.CharField(max_length=100)
	number_plate = models.CharField(max_length=100)
	bus_route_number = models.CharField(max_length=100)
	teacher_incharge = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = "buses"    

	def __str__(self):
		return self.bus_route_number


class Student(models.Model):
	bus = models.ForeignKey(Bus, on_delete=models.PROTECT) #on deleteing a bus, first delete the students manually else bus cant be deleted
	
	admission_number = models.PositiveIntegerField(unique=True)
	student_name = models.CharField(max_length=100)
	parent_name = models.CharField(max_length= 100)
	class_number = models.PositiveIntegerField(validators = [MinValueValidator(1), MaxValueValidator(12)])
	section = models.CharField(max_length = 1)
	phone_number = PhoneNumberField()
	email_id = models.EmailField()
	student_bus_stop = models.CharField(max_length=200)
	latitude = models.DecimalField(max_digits=10, decimal_places=8, null = True)
	longitude = models.DecimalField(max_digits=11, decimal_places=8, null = True)
	start_trip = models.DateTimeField(auto_now_add=False, null = True)
	end_trip = models.DateTimeField(auto_now_add=False, null = True)
	student_biometric_id = models.PositiveIntegerField(validators = [MinValueValidator(1), MaxValueValidator(255)])


	def Meta(self):
		unique_together = ("student_biometric_id", "bus")

	def __str__(self):
		return str(self.admission_number) + " - " + self.student_name
