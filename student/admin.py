from django.contrib import admin
from.models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display = ("first_name","last_name","registration_number","email","date_joined","profile_picture")
	search_fields = ("registration_number","email","last_name")
	list_filter = ("date_joined","date_of_birth")
admin.site.register(Student,StudentAdmin)