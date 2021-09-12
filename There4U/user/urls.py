from django.urls import path
from django.urls.resolvers import URLPattern
from .views import user_view

app_name = 'user'

urlpatterns = [
    path('', user_view, name="user"),
    # path('<int:pk>/', user_view, name="user")

]