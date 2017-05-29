from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

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
	# owner = models.ForeignKey('auth.User', related_name='students')
	student_name = models.CharField(max_length=100)
	parent_name = models.CharField(max_length= 100)
	class_number = models.PositiveIntegerField(validators = [MinValueValidator(1), MaxValueValidator(12)])
	section = models.CharField(max_length = 1)
	student_photo =  models.FileField()
	phone_number = PhoneNumberField()
	student_bus_stop = models.CharField(max_length=200)
	latitude = models.DecimalField(max_digits=10, decimal_places=8)
	longitude = models.DecimalField(max_digits=11, decimal_places=8)
	start_trip = models.DateTimeField(auto_now=True, auto_now_add=False)
	end_trip = models.DateTimeField(auto_now=True, auto_now_add=False)
	student_id = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.student_name

	# def save(self, force_insert=False, force_update=False):
	# 	self.student_id += 1

	# 	super(Student, self).save(force_insert, force_update) # Call the "real" save() method.


	def save(self, *args, **kwargs):
		obj = super(Student, self).save(*args, **kwargs)
		try:
			last_student_id = self.bus.student_set.all().order_by('-student_id')[0]
		except KeyError:
			pass
		else:
			Student.objects.filter(id=self.id).update(student_id=last_student_id.student_id+1)
		return obj




			