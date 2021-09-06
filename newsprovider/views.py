from rest_framework import generics, permissions
from newsprovider.models import Author, Article
from newsprovider.serializers import AuthorSerializer, ArticleSerializer, UserSerializer, ArticleRetrieveSerializer, ArticleCreateSerializer, ArticleAdminRetrieveSerializer
from django.contrib.auth.models import User

# authors
class AuthorList(generics.ListCreateAPIView):
  permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticated)
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticated)
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer

# articles
class ArticleList(generics.ListCreateAPIView):
  permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticated)
  queryset = Article.objects.all()
  
  def get_serializer_class(self):
      if self.request.method == "GET":
        return ArticleSerializer
      else:
        return ArticleCreateSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticated)
  queryset = Article.objects.all()
  serializer_class = ArticleSerializer
  
class ArticleRetrieveView(generics.RetrieveAPIView):
  queryset = Article.objects.all()
  
  def get_serializer_class(self):
    if self.request.user.is_authenticated:
      return ArticleAdminRetrieveSerializer
    else:
      return ArticleRetrieveSerializer
  
class ArticleListView(generics.ListAPIView):
  serializer_class = ArticleSerializer
  
  def get_queryset(self):
    category = self.request.query_params.get('category', None)
    
    if (category is not None):
      return Article.objects.filter(category=category)  
    
    return Article.objects.all()

# account
class UserCreate(generics.CreateAPIView):
  permission_classes = (permissions.AllowAny, )
  queryset = User.objects.all()
  serializer_class = UserSerializer
  
class UserList(generics.ListAPIView):
  permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticated)
  queryset = User.objects.all()
  serializer_class = UserSerializer