from rest_framework import serializers
from api import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = 'id','name'

class ToySerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    imageURL = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    category = CategorySerializer()
