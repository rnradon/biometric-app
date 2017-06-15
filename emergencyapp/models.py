from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class EmergencyContact(models.Model):
	contact_name = models.CharField(max_length=100)
	phone_number = PhoneNumberField()
	email_id = models.EmailField()


	def __str__(self):
		return self.contact_name