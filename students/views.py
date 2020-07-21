from core.views import BaseViewSet
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(BaseViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
