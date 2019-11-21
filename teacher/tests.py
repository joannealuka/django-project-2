from django.test import TestCase
from .models import Teacher
import datetime
from .forms import TeacherForm
from django.urls import reverse
from django.test import Client


class CreateTeacherTestCase(TestCase):
        def setUp(self):
            self.data={
                "first_name":"Joan",
                "last_name":"Aluka",
                "date_of_birth":datetime.date(2000,7,10),
                "registration_no":"123",
                "email":"mmbonojoan@gmail.com",
                "phone_number":"0718149079",
                "place_of_residence":"Nairobi",
                "id_number":1234,
                "profession":"Frontend developer",
                
            }
            self.bad_data={
                "first_name":"Joan",
                "last_name":"Ala",
                "date_of_birth":datetime.date(2000,7,10),
                "registration_number":"123",
                "email":"mmbonojoan@gmail.com",
                "phone_number":"0718149079",
                "place_of_residence":"Nairobi",
                "profession":"Frontend developer",
                "id_number":1234,
               
            }

        def test_teacher_form_accepts_valid_data(self):
            form =TeacherForm(self.data)
            self.assertTrue(form.is_valid())

        def test_teacher_form_rejects_invalid_data(self):
            form =TeacherForm(self.bad_data)
            self.assertFalse(form.is_valid())

        def test_add_teacher_view(self):
           url = reverse("add_teacher")
           request=client.post (url,self.data)
           self.assertEqual(request.status_code,200)

        def test_add_bad_view(self):
           url = reverse("add_teacher")
           request=client.post (url,self.bad_data)
           self.assertEqual(request.status_code,400)


# Create your tests he


# Create your tests here.
