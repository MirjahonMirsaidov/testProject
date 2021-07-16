from rest_framework import serializers

from .models import Items, Samples, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ItemsSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Items
        fields = ('id', 'name', 'quantity', 'rank', 'categories', 'verified')
