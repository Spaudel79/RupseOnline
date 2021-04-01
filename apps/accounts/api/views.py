from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework import viewsets, mixins, response, status
from rest_framework.permissions import (
AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly,
)
from rest_framework.generics import (GenericAPIView,CreateAPIView, ListCreateAPIView,UpdateAPIView,
ListAPIView,RetrieveAPIView)
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
        serializer.save(request)
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

class SellerRegisterView(RegisterUserView):
    serializer_class = SellerRegisterSerializer

    # def create(self, validated_data):
    #     seller = Seller.objects.create(seller=self.request.user,
    #                                phone_num=self.cleaned_data.get('phone_num'))



class SellerLoginUserView(LoginView):
    permission_classes = [AllowAny]
    serializer_class = SellerLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = SellerLoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        new_data = serializer.data
        user = serializer.validated_data["user"]
        serializer = self.get_serializer(user)
        token, created = Token.objects.get_or_create(user=user)
        # return response.Response(new_data, status=status.HTTP_200_OK)
        return response.Response({"token": token.key,
                                  "serializer.data": serializer.data},
                                   status=status.HTTP_200_OK)

class SellerProfileView(ListAPIView):
    permission_classes = [IsAuthenticated]
    # queryset = Seller.objects.filter(pk=pk)
    serializer_class = SellerProfileSerializer

    def get_queryset(self):
        queryset = Seller.objects.filter(seller=self.request.user)
        return queryset


class SellerUpdateProfileView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = SellerProfileUpdateSerializer

    # def perform_update(self, serializer):
    #     user = self.request.user
    #     seller = get_object_or_404(Seller, pk=self.kwargs['pk'])
    #     serializer.save(user=user, seller=seller)

class SellerTokenView(ListAPIView):
    def get(self, request, *args, **kwargs):
        serializer = CustomUserDetailsSerializer(request.user)
        return Response({"user": serializer.data})

class CustomerRegisterView(RegisterView):
    serializer_class = CustomerRegisterSerializer


class CustomerLoginUserView(LoginView):
    permission_classes = [AllowAny]
    serializer_class = CustomerLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CustomerLoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        new_data = serializer.data
        user = serializer.validated_data["user"]
        serializer = self.get_serializer(user)
        token, created = Token.objects.get_or_create(user=user)
        # return response.Response(new_data, status=status.HTTP_200_OK)
        return response.Response({"token": token.key,
                                  "serializer.data": serializer.data},
                                   status=status.HTTP_200_OK)

class CustomerProfileView(ListAPIView):
    permission_classes = [IsAuthenticated]
    # queryset = Seller.objects.filter(pk=pk)
    serializer_class = CustomerProfileSerializer

    def get_queryset(self):
        queryset = Customer.objects.filter(customer=self.request.user)
        return queryset

class CustomerUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = CustomerUpdateSerializer

class CustomerTokenView(ListAPIView):
    def get(self, request, *args, **kwargs):
        serializer = CustomUserDetailsSerializer(request.user)
        return Response({"user": serializer.data})

class Logout(GenericAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
