import unittest

# Create your tests here.

from news.models import News, Category

class NewsModelTest(unittest.TestCase):

    @classmethod
    def setUpTestData(cls):
        News.objects.create(title='Test', content='Test-test-test', is_published=True, category=2)
        News.objects.create(title='Test 2', content='Test-test-test 2', is_published=True, category=1)

    def test_get_absolute_url(self):
        news=News.objects.get(id=1)
        self.assertEquals(news.get_absolute_url(), '/news/1/')

class CategoryModelTest(unittest.TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(title='Test')
        Category.objects.create(title='Test 2')

    def test_get_absolute_url(self):
        cats=Category.objects.get(id=1)
        self.assertEquals(cats.get_absolute_url(), '/category/1/')