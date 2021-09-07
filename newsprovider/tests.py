from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from newsprovider.models import Author, Article


class NewsProviderTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username="testuser1", password="abc123")
        testuser1.save()

        test_author = Author.objects.create(name="Eric")

        Article.objects.create(
            author=test_author,
            category="Horror",
            title="Horror Eric",
            summary="Summary 1",
            first_paragraph="First P",
            body="Here lays a body",
        )

    def test_news_author(self):
        author = Author.objects.get(id=1)
        name = f"{author.name}"
        self.assertEqual(name, "Eric")

    def test_news_article(self):
        article = Article.objects.get(id=1)
        author = article.author.name
        category = f"{article.category}"
        title = f"{article.title}"
        summary = f"{article.summary}"
        first_paragraph = f"{article.first_paragraph}"
        body = f"{article.body}"
        self.assertEqual(author, "Eric")
        self.assertEqual(category, "Horror")
        self.assertEqual(title, "Horror Eric")
        self.assertEqual(summary, "Summary 1")
        self.assertEqual(first_paragraph, "First P")
        self.assertEqual(body, "Here lays a body")


class AccountTests(APITestCase):
    def test_user_registration(self):
        url = reverse("sign-up")
        data = {
            "username": "testcase1",
            "email": "test@localhost.app",
            "password": "strong_password",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def setUp(self):
        self.user = User.objects.create_user(
            username="testcase", password="strong_password"
        )

    def test_user_login(self):
        url = reverse("login")
        data = {"username": "testcase", "password": "strong_password"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_list(self):
        url = reverse("users")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ArticleTests(APITestCase):
    def setUp(self):
        test_author = Author.objects.create(name="Eric")

        Article.objects.create(
            author=test_author,
            category="TestCase",
            title="Test Case Eric",
            summary="Test summary 1",
            first_paragraph="First P 1",
            body="Here lays a body 1",
        )

        Article.objects.create(
            author=test_author,
            category="Horror",
            title="Horror Eric 2",
            summary="Test summary 2",
            first_paragraph="First P 2",
            body="Here lays a body 2",
        )

    def test_list_articles(self):
        url = reverse("articles")
        response = self.client.get(url)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_filter_articles(self):
        response = self.client.get("/api/articles/?category=TestCase")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
