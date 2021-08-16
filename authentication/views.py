from rest_framework.generics import GenericAPIView

from authentication.serializers import RegisterSerializer


class RegisterView(GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()