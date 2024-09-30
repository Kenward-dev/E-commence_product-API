from rest_framework import serializers
from .models import Product
from taggit.serializers import (TagListSerializerField, TaggitSerializer)

class ProductSerializer(TaggitSerializer, serializers.ModelSerializer):
    category = TagListSerializerField()
    formatted_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'formatted_price', 'stock_quantity', 'image_url', 'category', 'seller', 'created_at', 'updated_at']
        read_only_fields = ['seller', 'formatted_price', 'created_at', 'updated_at']

    def get_formatted_price(self, obj):
        return f"${obj.price:.2f}"

    def create(self, validated_data):
        category = validated_data.pop('category', [])
        instance = super().create(validated_data)
        instance.category.add(*category)
        return instance

    def update(self, instance, validated_data):
        category = validated_data.pop('category', None)
        instance = super().update(instance, validated_data)
        if category is not None:
            instance.category.set(category)
        return instance

    def validate_stock_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError('Stock quantity cannot be less than 0.')
        return value