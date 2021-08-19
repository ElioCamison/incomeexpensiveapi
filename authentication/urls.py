from django.urls import path

from .views import RegisterView, VerifyEmail, LoginAPIvIEW

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIvIEW.as_view(), name='login'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify')
]