from django.contrib import admin
from.models import Course
class CourseAdmin(admin.ModelAdmin):
	list_display = ("name","duration_in_months","course_number","description")
	search_fields = ("name","description","teacher__first_name","teacher__email","teacher__registration_no","course_number")
	list_filter = ("teacher__first_name",)
admin.site.register(Course,CourseAdmin)
