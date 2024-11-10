from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken, AuthenticationFailed

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
            return Response({'message': 'Usuário não encontrado.'}, status=status.HTTP_401_UNAUTHORIZED)
        except TokenError as e:
            return Response({'message': str(e.args[0])}, status=status.HTTP_400_BAD_REQUEST)
            #raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

