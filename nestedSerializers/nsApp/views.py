from django.shortcuts import render
from .models import Author,Book
from nsApp.serializers import BookSerializer,AuthorSerializer
from rest_framework import generics


class AuthorListView(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
    
class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class BookListView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer