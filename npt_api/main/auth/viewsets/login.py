from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.exceptions import AuthenticationFailed
from main.auth.serializers import LoginSerializer

class LoginViewSet(ViewSet):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except AuthenticationFailed as e:
            return Response({'message': 'Usuário e/ou senha incorretos!'}, status=status.HTTP_401_UNAUTHORIZED)
        except serializers.ValidationError as e:
            return Response({'message': str(e.detail)}, status=status.HTTP_400_BAD_REQUEST)


        return Response(serializer.validated_data, status=status.HTTP_200_OK)

