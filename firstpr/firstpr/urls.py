"""
URL configuration for firstpr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from start import views
from focus import views as focus_views

urlpatterns = [
    path('focus/articles/list/',focus_views.focus_list_view,name = 'list_url'),
    path('focus/articles/list/<str:url>/',focus_views.urls_view,name = 'articles_url'),
    path('admin/', admin.site.urls, name='admin'),  # Исправлено имя для admin
    path('', views.entrance_view, name='home'),
    path('regis/', views.registration_view, name='registration'),
    path('focus/', views.focus_view, name='focus_p'),
    path('focus/articles/', focus_views.articles_view, name='articles')
]