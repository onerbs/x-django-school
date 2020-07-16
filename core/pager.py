from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
	page_size = 3
	page_size_query_param = 'size'
	max_page_size = 10
