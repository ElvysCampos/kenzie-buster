from django.urls import path
from .views import UsersView, UsersDetailsView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('users/', UsersView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path('users/<int:user_id>/', UsersDetailsView.as_view()),
]
