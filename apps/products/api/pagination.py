from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from rest_framework.response import Response

class ProductPageNumberPagination(PageNumberPagination):
    page_size = 1


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'page_size' : 15,
            'results': data
        })