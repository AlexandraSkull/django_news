from django.conf import settings
from django.urls import reverse
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Category')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categoryes'
        ordering = ['title']

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Photo', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    watch_users = models.IntegerField(default=0, verbose_name='Views')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
        ordering = ['-created_at']

