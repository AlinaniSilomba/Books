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
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def AddBook(request):
 if request.method == 'POST':
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def GetBook(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def UpdateBook(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def DeleteBook(request, pk):
    if request.method == 'DELETE':
         try:
             book = Book.objects.get(pk=pk)
         except Book.DoesNotExist:
             return Response(status=status.HTTP_400_NOT_FOUND)
    serializer = BookSerializer(Book,data=request.data)
    if serializer.is_valid():
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    
        
   
        
        
