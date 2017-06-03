from django.contrib import admin
from .models import Bus, Student
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from . import urls

# Register your models here.

# admin.site.register(Student)

class StudentAdmin(admin.ModelAdmin):
	exclude = ('start_trip', 'end_trip', 'latitude', 'longitude')
	def response_add(self, request, obj, post_url_continue=None):
		"""This makes the response after adding go to another apps changelist for some model"""
		return HttpResponseRedirect("/rest-auth/registration")


# class ModelAdmin(admin.ModelAdmin):
	

admin.site.register(Student, StudentAdmin)
admin.site.register(Bus)