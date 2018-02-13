from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.exceptions import PermissionDenied

from .serializers import UserSerializer
from .serializers import UserPasswordSerializer
from .permissions import IsAdminOrSelf


class UserList(generics.ListCreateAPIView):
    """
    get:
        Retorna lista de Usuarios.
    post:
        Crea Usuario.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
        Retorna Usuario.
    put:
        Modifica Usuario.
    delete:
        Borra Usuario.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAdminOrSelf)


class UserPasswordDetail(generics.UpdateAPIView):
    """
    put:
        Modifica contraseña de usuario.
    """
    permission_classes = (IsAuthenticated,
                          IsAdminOrSelf)

    queryset = User.objects.all()
    serializer_class = UserPasswordSerializer

    def update(self, request, pk, partial=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(pk=pk)
        self.check_object_permissions(request, user)

        if('password' in serializer.validated_data):
            password = serializer.validated_data['password']
        else:
            password = None

        # if (request.user.id == int(pk) and
        #         not user.check_password(password)):
        #     raise PermissionDenied()

        password_new = serializer.validated_data['password_new']
        try:
            validate_password(password_new)
        except Exception as error:
            msg = ''.join(error)
            return Response(status=status.HTTP_400_BAD_REQUEST, data=msg)

        user.set_password(password_new)
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class Logout(APIView):
    """
    get:
        Elimina token(si existe)
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        if(hasattr(request.user, 'auth_token')):
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CheckToken(APIView):
    """
    get:
        Retorna usuario actual
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, format=None):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data)
