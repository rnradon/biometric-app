from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class GovtEmergencyContact(models.Model):
	contact_name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=100)


	def __str__(self):
		return self.contact_name

	