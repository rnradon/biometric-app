from rest_framework import serializers
from .models import Bus, Student

class StudentSerializer(serializers.ModelSerializer):

	# owner = serializers.CharField(source='owner.username')

	class Meta:
		model = Student
		fields = '__all__'


		#fiels = ('studnet_name, parent_name')

class BusSerializer(serializers.ModelSerializer):

	# owner = serializers.CharField(source='owner.username')

	class Meta:
		model = Bus
		fields = '__all__'


		#fiels = ('studnet_name, parent_name')

# class SignUpSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#         write_only_fields = ('password',)
