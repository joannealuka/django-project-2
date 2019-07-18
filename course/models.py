from django.db import models
from teacher.models import Teacher

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=50)
	duration_in_months = models.SmallIntegerField()
	course_number = models.CharField(max_length=50)
	description = models.TextField()

	teacher = models.ForeignKey(Teacher,on_delete=models.PROTECT)

	def __str__(self):
		return self.name