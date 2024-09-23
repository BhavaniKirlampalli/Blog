from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('register/', views.register, name='register'),
     path('post/<int:pk>/', views.post_detail, name='post-detail'),
]
