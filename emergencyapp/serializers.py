from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError

from .models import EmergencyContact



class EmergencyContactSerializer(serializers.ModelSerializer):

	class Meta:
		model = EmergencyContact
		fields = '__all__'