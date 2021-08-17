from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.serializers import RegisterSerializer


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = RefreshToken.for_user(user)
        current_site = get_current_site(request).domain
        path = reverse('email-verify')
        url = f'https://{current_site}{path}'

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VerifyEmail(GenericAPIView):

    def get(self, request):
        pass