from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError

from .models import GovtEmergencyContact



class GovtEmergencyContactSerializer(serializers.ModelSerializer):

	class Meta:
		model = GovtEmergencyContact
		fields = '__all__'