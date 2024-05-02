from django.contrib import admin
from django.urls import path
from .views import index
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index, name='index'),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('about/', views.about, name='about'),
]