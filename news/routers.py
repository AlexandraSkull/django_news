from rest_framework import routers

from news import views

def get_routers():
    router = routers.DefaultRouter()
    router.register(r'women', views.NewsViewSet(), basename='news')
    return router