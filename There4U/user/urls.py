from django.urls.conf import path
from user.views import UserLoginView, UserViewSet, UserLogoutView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout")
]
urlpatterns += router.urls 