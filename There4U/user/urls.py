from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework import views
from user import views

app_name = 'user'

urlpatterns = [
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UserDetail.as_view()),
]