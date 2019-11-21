from django.test import TestCase
from .models import Student
import datetime
from .forms import StudentForm
from django.urls import reverse
from django.test import Client

client=Client()
class StudentTestCase(TestCase):
    def setUp(self):
        self.student=Student(
            first_name="Joan",
            last_name="Aluka",
            date_of_birth=datetime.date(2000,7,10),
            registration_number="123",
            email="mmbonojoan@gmail.com",
            phone_number="0718149079",
            place_of_residence="Nairobi",
            guardian_phone="12334",
            id_number=1234,
            date_joined=datetime.date.today(),
            )
    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())

    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name,self.student.full_name())

    def test_age_is_always_17(self):
        self.assertFalse(self.student.clean() <17)

    def test_age_is_below_30(self):
        self.assertFalse(self.student.clean()>30)

class CreateStudentTestCase(TestCase):
        def setUp(self):
            self.data={
                "first_name":"Joan",
                "last_name":"Aluka",
                "date_of_birth":datetime.date(2000,7,10),
                "registration_number":"123",
                "email":"mmbonojoan@gmail.com",
                "phone_number":"0718149079",
                "place_of_residence":"Nairobi",
                "guardian_phone":"12334",
                "id_number":1234,
                "date_joined":datetime.date.today(),
            }
            self.bad_data={
                "first_name":"",
                "last_name":"Aluka",
                "date_of_birth":datetime.date(2000,7,10),
                "registration_number":"123",
                "email":"mmbonojoan@gmail.com",
                "phone_number":"0718149079",
                "place_of_residence":"Nairobi",
                "guardian_phone":"12334",
                "id_number":1234,
                "date_joined":datetime.date.today(),
            }

        def test_student_form_accepts_valid_data(self):
            form =StudentForm(self.data)
            self.assertTrue(form.is_valid())

        def test_student_form_rejects_invalid_data(self):
            form =StudentForm(self.bad_data)
            self.assertFalse(form.is_valid())

        def test_add_student_view(self):
            url=reverse("add_student")
            request=client.post(url,self.data)
            self.assertEqual(request.status_code,200)

        def test_add_student_invalid_data(self):
            url=reverse("add_student")
            request=client.post(url,self.bad_data)
            self.assertEqual(request.status_code,400)
# Create your tests he
