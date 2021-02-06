from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_auth.serializers import LoginSerializer
from rest_auth.registration.serializers import RegisterSerializer
from ..models import *
from django.db.models import Q


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


class SellerRegisterSerializer(RegisterSerializer):
    seller = serializers.PrimaryKeyRelatedField(read_only=True,)
    phone_num = serializers.CharField(required=False)
    username = None
    business_name = serializers.CharField(required=False)
    legal_name = serializers.CharField(required=False)
    company_registration_name = serializers.CharField(required=False)
    business_registration_no = serializers.CharField(required=False)
    business_email = serializers.EmailField(required=False)
    docs = serializers.FileField(required=False)
    full_name = serializers.CharField(required=False)
    mob_num = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    district = serializers.CharField(required=False)
    vdc = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    # password2 = serializers.CharField(allow_null=True,allow_blank=True)
    # password2= None

    # class Meta:
    #     model = User
    #     fields = ['seller','email', 'phone_num', 'first_name', 'last_name', 'password']

    def get_cleaned_data(self):
        data = super(SellerRegisterSerializer, self).get_cleaned_data()
        extra_data = {
            'phone_num': self.validated_data.get('phone_num', ''),
            'business_name': self.validated_data.get('business_name', ''),
            'legal_name': self.validated_data.get('legal_name', ''),
            'company_registration_name': self.validated_data.get('company_registration_name', ''),
            'business_registration_no': self.validated_data.get('business_registration_no', ''),
            'business_email': self.validated_data.get('business_email', ''),
            'docs': self.validated_data.get('docs', ''),
            'full_name': self.validated_data.get('full_name', ''),
            'mob_num': self.validated_data.get('mob_num', ''),
            'state': self.validated_data.get('state', ''),
            'district': self.validated_data.get('district', ''),
            'vdc': self.validated_data.get('vdc', ''),
            'address': self.validated_data.get('address', ''),


        }
        data.update(extra_data)
        return data

    def save(self,request,**kwargs):

        user = super(SellerRegisterSerializer,self).save(request)
        # user = super().save()
        user.is_seller = True
        user.save()
        seller = Seller(seller=user,
                        phone_num=self.cleaned_data.get('phone_num'),
                        business_name=self.cleaned_data.get('business_name'),
                        legal_name=self.cleaned_data.get('legal_name'),
                        company_registration_name=self.cleaned_data.get('company_registration_name'),
                        business_registration_no=self.cleaned_data.get('business_registration_no'),
                        business_email=self.cleaned_data.get('business_email'),
                        docs =self.cleaned_data.get('docs'),
                        full_name=self.cleaned_data.get('full_name'),
                        mob_num=self.cleaned_data.get('mob_num'),
                        state=self.cleaned_data.get('state'),
                        district=self.cleaned_data.get('district'),
                        vdc=self.cleaned_data.get('vdc'),
                        address=self.cleaned_data.get('address'),)

        seller.save()
        # content ={
        #     "seller":seller,
        #     "user": user
        # }
        return user

class SellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Seller
        fields = '__all__'
        depth = 1

class SellerLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label='Email Address')

    class Meta:
        model = User
        fields = [
            'id', 'email', 'password',
        ]
        # fields = '__all__'
        extra_kwargs = {"password":
                            {"write_only": True}}

    def validate(self, data):
        user = None
        email = data.get("email", None)
        password = data.get("password")
        if not email:
            raise serializers.ValidationError("Email is required for login")
        if not password:
            raise serializers.ValidationError("Password is required for login")
        user = User.objects.filter(Q(email=email)).distinct()
        if user.exists() and user.count() ==1:
            user = user.first()
        else:
            raise serializers.ValidationError("This email is not valid")
        if user:
            if not user.check_password(password):
                raise serializers.ValidationError("Incorrect password")
            if not user.is_seller:
                raise serializers.ValidationError("This is not lol seller account")

        data['user'] = user

        return data




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
