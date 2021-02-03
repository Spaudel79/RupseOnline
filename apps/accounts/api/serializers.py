from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_auth.serializers import LoginSerializer
from rest_auth.registration.serializers import RegisterSerializer
from ..models import *


try:
    from allauth.utils import email_address_exists
    from allauth.account.adapter import get_adapter
    from allauth.account.utils import setup_user_email
except ImportError:
    raise ImportError("allauth needs to be added to INSTALLED_APPS.")

User = get_user_model()


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email")


class SellerRegisterSerializer(serializers.ModelSerializer):
    seller = serializers.PrimaryKeyRelatedField(read_only=True,)
    phone_num = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['seller','email', 'phone_num', 'first_name', 'last_name', 'password']


    def get_cleaned_data(self):
        data = super(SellerRegisterSerializer, self).get_cleaned_data()
        extra_data = {
            'phone_num': self.validated_data.get('phone_num', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request,*args, **kwargs):
        user = super(self).save(request)
        # user = super().save()
        user.is_seller = True
        user.save()
        seller = Seller(seller=user,
                        phone_num=self.cleaned_data.get('phone_num'))
        seller.save(*args, **kwargs)
        return user


class CustomLoginSerializer(LoginSerializer):
    # username = None
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={"input_type": "password"},)
    # user_type = serializers.IntegerField()

    # fields = ("email", "password", "user_type")




class CustomRegisterSerializer(serializers.Serializer):
    """
    Modified RegisterSerializer class from rest_auth
    """

    username = None
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True, style={"input_type": "password"})
    password2 = serializers.CharField(write_only=True, style={"input_type": "password"})

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and email_address_exists(email):
        # if email:
            raise serializers.ValidationError(
                "A user is already registered with this e-mail address."
            )
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("The two password fields didn't match.")
        return data

    def get_cleaned_data(self):
        return {
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "password1": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        return user
