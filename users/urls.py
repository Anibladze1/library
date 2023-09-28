from django.urls import path
from .views import RegisterAPIView, LoginAPIView, LogoutAPIView, DeleteUserAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('delete/<int:user_id>/', DeleteUserAPIView.as_view(), name='delete-user'),
]
