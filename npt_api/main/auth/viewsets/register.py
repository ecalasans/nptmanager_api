from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from main.auth.serializers import RegisterSerializer

class RegisterViewSet(ViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    http_method_names = ['post']

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        if user:
            refresh = RefreshToken.for_user(user)

            response = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return Response(
                {
                    "user":  serializer.data,
                    "refresh": response['refresh'],
                    "access": response['access'],
                    "message": "Usuário cadastrado com sucesso!",
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {
                    "message":  "Ocorreu algum erro no servidor!  Tente mais tarde!"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
