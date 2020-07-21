from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class BaseViewSet(viewsets.ModelViewSet):

	@action(detail=False, methods=['GET'])
	def reverse(self, request):
		objects = self.get_queryset().order_by('-id')
		serialized = self.get_serializer_class()(objects, many=True)
		return Response(status=HTTP_200_OK, data=serialized.data)
