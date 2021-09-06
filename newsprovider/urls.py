from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from newsprovider.views import AuthorList, AuthorDetail, ArticleList, ArticleDetail, ArticleListView, UserCreate, UserList, ArticleRetrieveView

urlpatterns = [
  # admin authors CRUD
  path('admin/authors/<int:pk>/', AuthorDetail.as_view(), name='admin_authors_id'),
  path('admin/authors/', AuthorList.as_view(), name='admin_authors'),
  
  # admin articles CRUD
  path('admin/articles/<int:pk>/', ArticleDetail.as_view(), name='admin_articles_id'),
  path('admin/articles/', ArticleList.as_view(), name='admin_articles'),
  
  # articles
  path('articles/', ArticleListView.as_view(), name='articles'),
  path('articles/<int:pk>/', ArticleRetrieveView.as_view(), name='articles_id'),
  
  # account
  path('admin/users/', UserList.as_view(), name='users'),
  path('sign-up/', UserCreate.as_view(), name='sign-up'),
  path('login/', obtain_auth_token, name='login')
]