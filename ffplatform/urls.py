"""ffplatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.views import generic
from rest_framework.routers import DefaultRouter
from fb_fetch import views as fb_fetch_views
from media_fetch import views as media_fetch_views

router = DefaultRouter()
router.register(r'fb_fetch', fb_fetch_views.Fb_fetchViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view2/', generic.TemplateView.as_view(template_name='view2.html')),
    path('', generic.TemplateView.as_view(template_name='view1.html')),
    path('about/', generic.TemplateView.as_view(template_name='view1.html')),
    path('catagory/', generic.TemplateView.as_view(template_name='view1.html')),
    path('api/', include(router.urls)),
    path('fb_cluster/', fb_fetch_views.index),
    path('news_cluster/', media_fetch_views.index),
]
