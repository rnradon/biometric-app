from django.contrib import admin
from .models import Bus, Student
from django.http import HttpResponseRedirect
from . import urls


from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from allauth.account.models import EmailAddress

# Register your models here.



class StudentAdmin(admin.ModelAdmin):
	exclude = ('start_trip', 'end_trip', 'latitude', 'longitude')
	def response_add(self, request, obj, post_url_continue=None):
		"""This makes the response after adding to redirect to user add admin"""
		return HttpResponseRedirect("/admin/auth/user/add/")

	def response_delete(self, request, obj, post_url_continue=None):
		"""This makes the response after deleting to redirect to user delete admin"""
		return HttpResponseRedirect("/admin/auth/user/")


# class ModelAdmin(admin.ModelAdmin):

class BusAdmin(admin.ModelAdmin):
	# exclude = ('start_trip', 'end_trip', 'latitude', 'longitude')
	def response_add(self, request, obj, post_url_continue=None):
		"""This makes the response after adding to redirect to signup form"""
		return HttpResponseRedirect("/scanapp/sign_up_bus")	



admin.site.register(Student, StudentAdmin)
admin.site.register(Bus, BusAdmin)

# admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.unregister(EmailAddress)
admin.site.unregister(Token)