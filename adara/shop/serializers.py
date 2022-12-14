from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


class SizeSerializer(serializers.Serializer):
    rus_size = serializers.CharField(max_length=10)
    int_size = serializers.CharField(max_length=10)


class ChemeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
