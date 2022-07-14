from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth import login, logout
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination

from .permissions import IsAdminReadOnly, IsOwnerOrReadOnly
from .models import Category, News
from .forms import NewsForm, UserRegisterForm, UserLoginForm
from .serializers import NewsSerializer

class ParentHome(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'
    paginate_by = 4

class HomeNews(ParentHome):
    def get_queryset(self):
        return News.objects.filter(is_published=True)

class NewsByCategory(ParentHome):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'],is_published=True)

def view_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    news_item.watch_users += 1
    news_item.save()
    return render(request, 'news/view_news.html', {'news_item': news_item})

def search_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        news = News.objects.filter(
            Q(title__contains=searched)| Q(content__contains=searched ))
        
        return render(request, 'news/home.html', {'news': news}) # rewrite search.html
    else:
        return render(request, 'news/home.html', {})

def add_news(request):
    if request.method=='POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.user = request.user
            news.save()
            form.save_m2m()
            return redirect('home_page')
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})

# User

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You register')
            return redirect('home_page')
        else:
            messages.error(request, 'Error')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_page')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

# REST FRAMEWORK

class NewsAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000

class NewsAPIList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = NewsAPIListPagination

class NewsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsOwnerOrReadOnly, )

class NewsAPIDetail(generics.RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminReadOnly, )



      