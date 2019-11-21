from django.test import TestCase
from student.models import Student
from course.models import Course
from teacher.models import Teacher
import datetime


class StudentCourseTestCase(TestCase):
    def setUp(self):
        self.student_a = Student.objects.create(
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


        self.student_b = Student.objects.create(
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

        self.python = Course.objects.create(
            name= "python",
            duration_in_months=6,
            course_number="5",
            description="python"
            )
        self.javaScript =Course.objects.create(
            name= "javaScript",
            duration_in_months=6,
            course_number="5",
            description="react js"

            )
        self.hardware = Course.objects.create(
            name= "hardware",
            duration_in_months=6,
            course_number="5",
            description="product design"
                
                
            )
                
        self.teacher = Teacher(
                first_name="Joan",
                last_name="Aluka",
                date_of_birth=datetime.date(2000,7,10),
                registration_no="123",
                email="mmbonojoan@gmail.com",
                phone_number="0718149079",
                place_of_residence="Nairobi",
                id_number=1234,
                profession="Frontend developer",
                
            ) 

    def test_student_can_join_many_courses(self):
        self.assertEqual(self.student_a.courses.count(), 0)
        self.student_a.courses.add(self.python)
        self.assertEqual(self.student_a.courses.count(), 1)
        self.student_a.courses.add(self.javascript)
        self.assertEqual(self.student_a.courses.count(), 2)
        self.student_a.courses.add(self.hardware)
        self.assertEqual(self.student_a.courses.count(), 3)
                    
    def test_course_can_join_many_students(self):
        self.python.students.add(self.student_a,self.student_b)
        self.assertEqual(self.python.students.count(), 2)

    def test_teacher_can_teach_many_courses(self):
        self.teacher_a.courses.add(self.python,self.javascript)
        self.assertEqual(self.teacher.courses.count(),2)

    def test_course_can_only_have_one_teacher(self):
        self.python.teacher=self.teacher_a
        self.assertEqual(self.python.teacher.name,"John")
        self.python.teacher =self.teacher_b
        self.assertEqual(self.python.teacher.name,"lan")

    def test_course_teacher_is_in_student_teachers_list(self):
        self.python.teacher=self.teacher_b
        self.student.courses.add(self.python)
        teachers=self.student.teachers()
        self.assertTrue(self.teacher_b in teachers)
        