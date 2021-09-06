from rest_framework import serializers
from newsprovider.models import Author, Article
from django.contrib.auth.models import User

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'name', 'picture')
    model = Author
    
class ArticleSerializer(serializers.ModelSerializer):
  author = AuthorSerializer()
  
  class Meta:
    fields = ('id', 'author', 'category', 'title', 'summary')
    model = Article

class ArticleAdminSerializer(serializers.ModelSerializer):
  author = AuthorSerializer()
  firstParagraph = serializers.CharField(source='first_paragraph')
  
  class Meta:
    fields = ('id', 'author', 'category', 'title', 'summary', 'firstParagraph', 'body')
    model = Article

class ArticleCreateSerializer(serializers.ModelSerializer):
  firstParagraph = serializers.CharField(source='first_paragraph')
  
  class Meta:
    fields = ('id', 'author', 'category', 'title', 'summary', 'firstParagraph', 'body')
    model = Article    
    
class ArticleRetrieveSerializer(serializers.ModelSerializer):
  author = AuthorSerializer()
  firstParagraph = serializers.CharField(source='first_paragraph')
  
  class Meta:
    fields = ('id', 'author', 'category', 'title', 'summary', 'firstParagraph')
    model = Article
    
class ArticleAdminRetrieveSerializer(serializers.ModelSerializer):
  author = AuthorSerializer()
  firstParagraph = serializers.CharField(source='first_paragraph')
  
  class Meta:
    fields = ('id', 'author', 'category', 'title', 'summary', 'firstParagraph', 'body')
    model = Article
       
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'email', 'password')
    extra_kwargs = {'password': {'write_only': True}}
    
  def create(self, validated_data):
    password = validated_data.pop('password')
    user = User(**validated_data)
    user.set_password(password)
    user.save()
    return user