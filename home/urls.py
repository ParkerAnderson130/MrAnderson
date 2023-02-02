from django.contrib import admin
from django.urls import path
from home import views
from .views import BlogView, BlogDetailView, ContactView

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', BlogView.as_view(), name="blog"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name="blog-detail"),
    path('contact/', ContactView.as_view(), name="contact"),
]