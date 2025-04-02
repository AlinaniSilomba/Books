from rest_framework import serializers
from .models import Book

# This serializer is used to serialize the data from the Book model.
# It is used to convert the data from the model to JSON format and vice versa.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'