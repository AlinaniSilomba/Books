from django.db import models

# This is the model that we will use to create the database table.
# # This model is used to create the database table for the books.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
   
    def __str__(self):
        return f'{self.title} by {self.author}'
    # This method is used to return the string representation of the model.