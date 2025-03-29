from django.urls import path
from . import views
#using class based views these are the urls that we will use to access the API endpoints.
urlpatterns = [
    path('books/', views.Books.as_view(), name='Books'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='BookDetail'),
]

#Using Function Based Views these are the urls that we will use to access the API endpoints.
"""
urlpatterns = [
    path('books/',views.GetAllBooks, name='GetAllBooks'),
    path('books/add/',views.AddBook, name='AddBook'),
    path('books/Getbook/<int:pk>/',views.GetBook, name='GetBook'),
    path('books/update/<int:pk>/',views.UpdateBook, name='UpdateBook'),
    path('books/delete/<int:pk>/',views.DeleteBook, name='DeleteBook'),
]
"""