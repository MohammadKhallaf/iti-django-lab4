from django.db import models


# Create your models here.
class Student(models.Model):
    gender = [("male", "male"),
              ("female", "female")]
    student_id = models.AutoField(primary_key=True)
    student_fname = models.CharField(max_length=10, default='unknown', verbose_name="fname")
    student_lname = models.CharField(max_length=10, default='unknown')
    student_email = models.EmailField(unique=True, default="email@email.com")
    student_gender = models.CharField(max_length=10, choices=gender, default="male")
    # student_passqwo


class Intake(models.Model):
    intake_id = models.AutoField(primary_key=True)
    intake_name = models.CharField(max_length=10)
    intake_start_date = models.DateField()
    intake_end_date = models.DateField(default="")
