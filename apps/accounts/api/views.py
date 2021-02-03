from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from .serializers import *
from rest_framework import viewsets, mixins, response, status
from rest_framework.permissions import (
AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly,
)
from rest_framework.generics import (GenericAPIView,CreateAPIView, ListCreateAPIView,
ListAPIView,)
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

# class CustomLoginView(LoginView):
#     pass
#
# class CustomRegisterView(RegisterView):
#     serializer_class = CustomRegisterSerializer


class RegisterUserView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = CustomRegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        return response.Response(user_data, status=status.HTTP_201_CREATED)

class LoginUserView(LoginView):
    permission_classes = [AllowAny]
    serializer_class = CustomLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CustomLoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        new_data = serializer.data
        user = serializer.validated_data["user"]
        serializer = self.get_serializer(user)
        token, created = Token.objects.get_or_create(user=user)
        # return response.Response(new_data, status=status.HTTP_200_OK)
        return response.Response({"token": token.key,
                                  "serializer.data": serializer.data},
                                   status=status.HTTP_200_OK)

class VendorLoginUserView(LoginView):
    permission_classes = [AllowAny]
    serializer_class = CustomLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CustomLoginSerializer(data=data)
        data['user_type'] = request.user.user_type
        user_type = data['user_type']

        if user_type == 2:
            serializer.is_valid(raise_exception=True)
            # new_data = serializer.data
            user = serializer.validated_data["user"]
            serializer = self.get_serializer(user)
            token, created = Token.objects.get_or_create(user=user)
            # return response.Response(new_data, status=status.HTTP_200_OK)
            return response.Response({"token": token.key,
                                      "serializer.data": serializer.data},
                                       status=status.HTTP_200_OK)

        else:
            print(user_type)
            message = "This is not a seller account"
            return Response({'message':message,},
                            status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
