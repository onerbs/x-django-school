from django.db import models

from students.models import Student


class Course(models.Model):
	name = models.CharField(max_length=50)
	students = models.ManyToManyField(Student, related_name='courses')

	def __str__(self):
		return self.name
