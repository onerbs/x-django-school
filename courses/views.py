from django.shortcuts import render

from .models import Course
from students.models import Student


def index(request):
    courses = Course.objects.all()

    for course in courses:
        course.slug = course.name.lower().replace(' ', '_')

    context = {
        'items': courses
    }

    return render(request, 'courses/index.html', context=context)


def list_members(request, slug):
    students = Student.objects.all()

    context = {
        'items': students
    }

    return render(request, 'courses/index.html', context=context)
