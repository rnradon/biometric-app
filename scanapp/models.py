from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import Permission, User

# Create your models here.

# class Bus(models.Model):
#     driver_name = models.CharField(max_length=100)
    


# class Student(models.Model):
#     bus = models.ForeignKey(Bus, on_delete=models.PROTECT) #on deleteing a bus, first delete the students manually else bus cant be deleted
#     student_name = models.CharField(max_length=100)
#     parent_name = models.CharField(max_length = 100)
# 	class_number = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(12)])
# 	section = models.CharField(max_length = 1)
# 	student_photo = models.FileField()
# 	phone_number = PhoneNumberField()
# 	lat = models.DecimalField(_('Latitude'), max_digits=10, decimal_places=8)
# 	lng = models.DecimalField(_('Longitude'), max_digits=11, decimal_places=8)
# 	#start_trip = models.


class Bus(models.Model):
	driver_name = models.CharField(max_length=100)
	conductor_name = models.CharField(max_length=100)
	number_plate = models.CharField(max_length=100)
	bus_number = models.CharField(max_length=100)
	teacher_incharge = models.CharField(max_length=100)

	def __str__(self):
		return self.bus_number


class Student(models.Model):
	bus = models.ForeignKey(Bus, on_delete=models.PROTECT) #on deleteing a bus, first delete the students manually else bus cant be deleted
	# owner = models.ForeignKey('auth.User', related_name='students', null = True)
	admission_number = models.PositiveIntegerField(unique=True)
	# username = models.PositiveIntegerField(blank=True, null = True)
	# password = models.CharField(max_length=100)
	student_name = models.CharField(max_length=100)
	parent_name = models.CharField(max_length= 100)
	class_number = models.PositiveIntegerField(validators = [MinValueValidator(1), MaxValueValidator(12)])
	section = models.CharField(max_length = 1)
	# student_photo =  models.FileField()
	phone_number = PhoneNumberField()
	student_bus_stop = models.CharField(max_length=200)
	latitude = models.DecimalField(max_digits=10, decimal_places=8, null = True)
	longitude = models.DecimalField(max_digits=11, decimal_places=8, null = True)
	start_trip = models.DateTimeField(auto_now=True, auto_now_add=False, null = True)
	end_trip = models.DateTimeField(auto_now=True, auto_now_add=False, null = True)
	student_id = models.PositiveIntegerField(default=0, editable = False)

	# user = User.objects.create(username=admission_number, password = "pass1234")
	# user.save()

	def __str__(self):
		return self.student_name

	# def save(self, force_insert=False, force_update=False):
	# 	self.student_id += 1

	# 	super(Student, self).save(force_insert, force_update) # Call the "real" save() method.


	def pre_save(self, *args, **kwargs):
		obj = super(Student, self).save(*args, **kwargs)
		try:
			last_student_id = self.bus.student_set.all().order_by('-student_id')[0]
		except KeyError:
			pass
		else:
			Student.objects.filter(id=self.id).update(student_id=last_student_id.student_id+1)
		return obj


	def get_readonly_fields(self, request, obj=None):
		return ['student_id ']
    	# return []

	# def save(self, *args, **kwargs):

	# 	self.owner.username = '{0}'.format( self.admission_number)
	# 	super(Student, self).save(*args, **kwargs)

#     
	def post_save(self, *args, **kwargs):
		user = User(username = '{0}'.format( self.admission_number))
		password = self.phone_number
		user.set_password(password)
		user.save()
		return user






			