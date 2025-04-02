from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .Serializers import BookSerializer
from rest_framework.views import APIView
from django.http import Http404


#Using class based views these are the urls that we will use to access the API endpoints.
 
class Books(APIView):
    #Here we are using the get method to get all the books from the database.
    #Here we are using the serializer to serialize the data and return it in JSON format.
        def get(self, request):
            book = Book.objects.all()
            serializer = BookSerializer(book, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        #Here we are using the post method to add a new book to the database.
        #Here we are using the serializer to validate the data and save it to the database.
        def post(self,request):
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    #Here we are using the get method to get a single book from the database.
    #Here we are using the serializer to serialize the data and return it in JSON format.
    #Here we are using the get_object method to get the book from the database by passing in the primary key pk.
    #Here we are using the Http404 to handle the exception if the book does not exist by importing it from django.http.
    def get_object(self, pk): 
       try:
         book = Book.objects.get(pk=pk)
         return book
       except Book.DoesNotExist:
           raise Http404
      #Here we are using the get method to get a single book from the database.
      #By using the get_object method to get the book from the database by passing in the primary key pk.
    def get(self,request,pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #Here we are using the put method to update a book in the database.
    #Here we are using the serializer to validate the data and save it to the database.
    #by first fetching the book from the database using the get_object method and then passing the data to the serializer.
    def put(self,request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #Here we are using the delete method to delete a book from the database.
    def delete(self,request,pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
       
"""  
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
"""
        
        
