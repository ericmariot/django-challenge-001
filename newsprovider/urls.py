from django.urls import path
from newsprovider.views import AuthorList, AuthorDetail, ArticleList, ArticleDetail, ArticleListCategory

urlpatterns = [
  # admin authors CRUD
  path('admin/authors/<int:pk>/', AuthorDetail.as_view()),
  path('admin/authors/', AuthorList.as_view()),
  
  # admin articles CRUD
  path('admin/articles/<int:pk>/', ArticleDetail.as_view()),
  path('admin/articles/', ArticleList.as_view()),
  
  # articles
  path('articles/', ArticleListCategory.as_view()),
]