from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.cache import cache_page
from django.conf.urls.static import static

from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cache_page(30) (views.HomeNews.as_view()), name='home_page'),
    path('category/<int:category_id>/', views.NewsByCategory.as_view(), name='category'),
    path('news/<int:news_id>/', views.view_news, name='view_news'),
    path('search/', views.search_results, name='search_results'),
    path('add_news/', views.add_news, name='add_news'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # rest_framework
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/new/', views.NewsAPIList.as_view()),
    path('api/v1/new/<int:pk>/', views.NewsAPIUpdate.as_view()),
    path('api/v1/new/detail/', views.NewsAPIDetail.as_view()),
    # djoser
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)