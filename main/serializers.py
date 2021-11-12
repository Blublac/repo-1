from django.db import models
from rest_framework import serializers
from .models import Student, Book

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
