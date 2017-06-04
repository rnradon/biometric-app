from django.contrib import admin
from .models import Bus, Student
# from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from . import urls


from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from allauth.account.models import EmailAddress

# Register your models here.

# admin.site.register(Student)

class StudentAdmin(admin.ModelAdmin):
	exclude = ('start_trip', 'end_trip', 'latitude', 'longitude')
	def response_add(self, request, obj, post_url_continue=None):
		"""This makes the response after adding go to another apps changelist for some model"""
		return HttpResponseRedirect("/scanapp/sign_up_student")


# class ModelAdmin(admin.ModelAdmin):

class BusAdmin(admin.ModelAdmin):
	# exclude = ('start_trip', 'end_trip', 'latitude', 'longitude')
	def response_add(self, request, obj, post_url_continue=None):
		"""This makes the response after adding go to another apps changelist for some model"""
		return HttpResponseRedirect("/scanapp/sign_up_bus")	

admin.site.register(Student, StudentAdmin)
admin.site.register(Bus, BusAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.unregister(EmailAddress)
admin.site.unregister(Token)