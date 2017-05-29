from rest_framework import serializers
from .models import Bus, Student

class StudentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Student
		fields = '__all__'


		#fiels = ('studnet_name, parent_name')
