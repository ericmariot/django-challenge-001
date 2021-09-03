from django.test import TestCase
from django.contrib.auth.models import User
from .models import Author, Article

class NewsProviderTests(TestCase):
  
  @classmethod
  def setUpTestData(cls):
    testuser1 = User.objects.create_user(
      username='testuser1', password='abc123')
    testuser1.save()
    
    test_author = Author.objects.create(
      name='Eric')
    
    test_article = Article.objects.create(
      author = test_author,
      category = 'Horror',
      title = 'Horror Eric',
      summary = 'Summary 1',
      first_paragraph = 'First P',
      body = 'Here lays a body')
    
  def test_news_author(self):
    author = Author.objects.get(id=1)
    name = f'{author.name}'
    self.assertEqual(name, 'Eric')
    
  def test_news_article(self):
    article = Article.objects.get(id=1)
    author = article.author.name
    category = f'{article.category}'
    title = f'{article.title}'
    summary = f'{article.summary}'
    first_paragraph = f'{article.first_paragraph}' 
    body = f'{article.body}'
    self.assertEqual(author, 'Eric')
    self.assertEqual(category, 'Horror')
    self.assertEqual(title, 'Horror Eric')
    self.assertEqual(summary, 'Summary 1')
    self.assertEqual(first_paragraph, 'First P')
    self.assertEqual(body, 'Here lays a body')