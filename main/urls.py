from django.urls import path

from .views import ItemsListView


urlpatterns = [
    path('item-list/', ItemsListView.as_view(), name='items-list')
]