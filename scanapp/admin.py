from django.contrib import admin
from .models import Bus, Student

# Register your models here.

# admin.site.register(Student)

class StudentAdmin(admin.ModelAdmin):
	exclude = ('student_id', )

admin.site.register(Student, StudentAdmin)
admin.site.register(Bus)