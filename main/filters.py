import django_filters
from django_filters import rest_framework as filters_rest

from main.models import Items, Samples


class ItemFilter(filters_rest.FilterSet):
    min_quantity = filters_rest.NumberFilter(field_name="quantity", lookup_expr='gte')
    max_quantity = filters_rest.NumberFilter(field_name="quantity", lookup_expr='lte')
    has_samples = django_filters.BooleanFilter(field_name='id', method='item_has_samples', label='has samples')

    def item_has_samples(self, queryset, field_name, value):
        if value:
            return queryset.filter(id__in=[sample.item_id for sample in Samples.objects.all()])
        return queryset

    class Meta:
        model = Items
        fields = ['verified', 'categories', 'min_quantity', 'max_quantity', 'has_samples']

