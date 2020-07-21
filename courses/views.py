from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from core.views import BaseViewSet
from students.serializers import StudentSerializer
from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(BaseViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

	@action(detail=True, methods=['GET'])
	def students(self, request, pk=None):
		course = self.get_object()
		students = course.students.all()
		serialized = StudentSerializer(students, many=True)
		return Response(status=status.HTTP_200_OK, data=serialized.data)
