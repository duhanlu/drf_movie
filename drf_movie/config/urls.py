"""
URL configuration for drf_movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movie import views
from account import views as accountView
from trade import views as cardView
from trade import views as tradeView

router = DefaultRouter()
router.register(r'movie', views.MovieViewSet, basename='movies')
router.register(r'category', views.CategoryViewSet, basename='category')
router.register(r'collects', accountView.CollectViewSet, basename='collects')
router.register(r'cards', cardView.CardViewSet)
router.register(r'orders', tradeView.OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/movie', include('movie.urls', namespace='movie'))
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.jwt')),
    path('api/alipay/', tradeView.AlipayAPIView.as_view()),
    path('api/callback/', tradeView.AlipayCallbackAPIView.as_view())
]
