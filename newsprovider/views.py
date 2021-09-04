from rest_framework import generics
from newsprovider.models import Author, Article
from newsprovider.serializers import AuthorSerializer, ArticleSerializer

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
  
class ArticleListCategory(generics.ListAPIView):
  serializer_class = ArticleSerializer
  
  def get_queryset(self):
    category = self.request.query_params.get('category', None)
    
    if (category is not None):
      return Article.objects.filter(category=category)  
    
    return Article.objects.all()  