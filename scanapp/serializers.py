from django.contrib.auth import get_user_model, authenticate
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import force_text

from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError


from .models import Bus, Student
from django.contrib.auth.models import User


from django.http import HttpRequest

try:
    from allauth.account import app_settings as allauth_settings
    from allauth.utils import (email_address_exists,
                               get_username_max_length)
    from allauth.account.adapter import get_adapter
    from allauth.account.utils import setup_user_email
except ImportError:
    raise ImportError("allauth needs to be added to INSTALLED_APPS.")

from requests.exceptions import HTTPError
from django.http import HttpResponseRedirect




class StudentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Student
		fields = '__all__'




class BusSerializer(serializers.ModelSerializer):


	class Meta:
		model = Bus
		fields = '__all__'






class RegisterSerializer(serializers.Serializer):

	username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )

	password1 = serializers.CharField(write_only=True)
	password2 = serializers.CharField(write_only=True)
	# email = serializers.EmailField(required=False)

	def validate_username(self, username):
		username = get_adapter().clean_username(username)
		return username

	def validate_password1(self, password):
		return get_adapter().clean_password(password)

	def validate(self, data):
		if data['password1'] != data['password2']:
			raise serializers.ValidationError(_("The two password fields din't match."))
		return data

	def custom_signup(self, request, user):
		pass

	def get_cleaned_data(self):
		return {
			'username': self.validated_data.get('username', ''),
			'password1': self.validated_data.get('password1', ''),
		}

	def save(self, request):
		adapter = get_adapter()
		user = adapter.new_user(request)
		self.cleaned_data = self.get_cleaned_data()
		adapter.save_user(request, user, self)
		self.custom_signup(request, user)
		return user


	

	

class EmailSerializer(serializers.Serializer):
	class Meta:
		model = Student
		fields = ('student_name', 'admission_number', 'parent_name', 'bus')




