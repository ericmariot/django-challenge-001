from rest_framework import serializers
from .models import Author, Article

class AuthorSerializer(serializers.ModelSerializer):
  
  class Meta:
    fields = ('id', 'name', 'picture', 'created_at',)
    model = Author
    
    
class ArticleSerializer(serializers.ModelSerializer):
  
  class Meta:
    fields = ('id', 'author', 'category', 'title', 'summary', 'first_paragraph', 'body', 'created_at',)
    model = Article