from django.urls import path
from . import views

urlpatterns = [
    path('books/',views.GetAllBooks, name='GetAllBooks'),
    path('books/add/',views.AddBook, name='AddBook'),
    path('books/Getbook/<int:pk>/',views.GetBook, name='GetBook'),
    path('books/update/<int:pk>/',views.UpdateBook, name='UpdateBook'),
    path('books/delete/<int:pk>/',views.DeleteBook, name='DeleteBook'),
]
