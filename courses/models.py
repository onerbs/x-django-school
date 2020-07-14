from django.db import models
from students.models import Student


class Course(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(Student)
