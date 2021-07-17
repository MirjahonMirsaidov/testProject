import django_filters
from rest_framework import generics, filters

from .filters import ItemFilter
from .models import Items
from .serializers import ItemsSerializer


class ItemsListView(generics.ListAPIView):
    serializer_class = ItemsSerializer
    queryset = Items.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', ]
    ordering_fields = []
    filterset_class = ItemFilter
    ordering = '-rank'


