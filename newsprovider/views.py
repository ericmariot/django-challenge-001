from rest_framework import generics
from .models import Author, Article
from .serializers import AuthorSerializer, ArticleSerializer

class AuthorList(generics.ListCreateAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer
  
class ArticleList(generics.ListCreateAPIView):
  queryset = Article.objects.all()
  serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Article.objects.all()
  serializer_class = ArticleSerializer