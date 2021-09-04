from django.urls import path
from .views import AuthorList, AuthorDetail, ArticleList, ArticleDetail

urlpatterns = [
  path('authors/<int:pk>/', AuthorDetail.as_view()),
  path('authors/', AuthorList.as_view()),
  path('articles/<int:pk>/', ArticleDetail.as_view()),
  path('articles/', ArticleList.as_view()),
]