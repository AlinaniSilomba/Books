from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .Serializers import BookSerializer


@api_view(['GET'])
def GetAllBooks(request):
    if request.method == 'GET':
    #Here we are getting the books from the database but this information is not serialized or translated in JSON format yet.
        books = Book.objects.all()
    #Here we are serializing the books into JSON format or converting the books into JSON format to be seen in the UI or frontend.
        serializer = BookSerializer(books, many=True)
    return Response(serializer.data)