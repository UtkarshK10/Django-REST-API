from django.db import models

# Create your models here.

class Author(models.Model):
    firstName=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    
    def __str__(self):
        return self.firstName+" "+self.lastname
    
class Book(models.Model):
    title=models.CharField(max_length=20)
    ratings=models.CharField(max_length=20)
    author=models.ForeignKey(Author,related_name='books',on_delete=models.CASCADE)
    