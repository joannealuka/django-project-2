from django.contrib import admin
from.models import Teacher
class TeacherAdmin(admin.ModelAdmin):
	list_display = ("first_name","last_name","registration_no","email","profession","profile_picture")
	search_fields = ("last_name","registration_no","email")
admin.site.register(Teacher,TeacherAdmin)
# Register your models here.