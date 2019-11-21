from django.db import models
from course.models import Course
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError

import datetime

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    registration_number = models.CharField(max_length=50)
    place_of_residence = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    guardian_phone = models.CharField(max_length=50)
    id_number = models.IntegerField()
    date_joined = models.DateField()
    profile_picture = models.ImageField(upload_to="student_image",blank=True,null=True)

    course = models.ManyToManyField(Course,blank=True,null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    def full_name(self):
        return "{} {}".format(
            self.first_name,
            self.last_name)
    def get_age(self):
     today =datetime.date.today()
     return  today.year- self.date_of_birth.year


    age=property(get_age)     

    def clean(self):
        age =self.age
        if age < 17 or age > 30:
            raise ValidationError("you  need to be above 17 years and below 30 years")
        return age
    def teachers(self):
        return[course.teacher for course in self.courses.all()]   
