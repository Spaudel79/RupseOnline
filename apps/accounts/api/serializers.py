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


class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerTestProfileSerializer(serializers.ModelSerializer):
    # customer = serializers.PrimaryKeyRelatedField()
    # first_name = serializers.CharField(required=False,read_only=True)
    # last_name = serializers.CharField(required=False,read_only=True)
    # phone_num = serializers.CharField(required=False,read_only=True)
    # region = serializers.CharField(required=False,read_only=True)
    # city = serializers.CharField(required=False,read_only=True)
    # area = serializers.CharField(required=False,read_only=True)
    # address = serializers.CharField(required=False,read_only=True)
    class Meta:
        model = Customer
        #fields = '__all__'
        fields = ['customer','first_name','last_name','phone_num','region','city','area','address']
        # depth = 1


class CustomerUpdateSerializer(serializers.ModelSerializer):
    customer = CustomerProfileSerializer()
    email = serializers.EmailField(required=False)
    class Meta:
        model = User
        fields = ('id', "first_name", "last_name",'email','customer')
        depth = 1

    def update(self, instance, validated_data):
        user = self.context['request'].user
        user.first_name = validated_data.get('first_name')
        user.last_name = validated_data.get('last_name')
        user.email = validated_data.get('email')
        # test = validated_data.get('email')
        # print(test)
        # # if user.email == test:
        # #     pass
        # # else:
        # #     user.email = validated_data.get('email')
        # # if user.email != validated_data.get('email'):
        # #     print(user.email)
        # #     user.email = validated_data.get('email')
        # # else:
        # #     pass
        # user.save()
        customer_data = validated_data.pop('customer',None)
        if customer_data is not None:
            instance.customer.first_name = customer_data['first_name']
            instance.customer.last_name = customer_data['last_name']
            instance.customer.phone_num = customer_data['phone_num']
            instance.customer.region = customer_data['region']
            instance.customer.city = customer_data['city']
            instance.customer.area = customer_data['area']
            instance.customer.address = customer_data['address']
            instance.customer.save()
        return super().update(instance,validated_data)

    # def update(self,request, instance, validated_data):
    #     customer_data = validated_data.pop('customer')
    #     user = self.request.user
    #     user.first_name = user.get('first_name')
    #     user.last_name = user.get('last_name')
    #     customer = instance.customer
    #     # instance.first_name = validated_data.get('first_name',instance.first_name)
    #     # instance.last_name = validated_data.get('last_name', instance.last_name)
    #
    #     instance.save()
    #     customer.region = customer_data.get('region',customer.region)
    #     customer.save()
    #     return instance

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    customer = CustomerProfileSerializer()
    class Meta:
        model = User
        #fields = '__all__'
        fields = ('id', 'password','email','is_seller','is_customer', 'customer')

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
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
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
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
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
                        first_name=self.cleaned_data.get('first_name'),
                        last_name=self.cleaned_data.get('last_name'),
                        mob_num=self.cleaned_data.get('mob_num'),
                        state=self.cleaned_data.get('state'),
                        district=self.cleaned_data.get('district'),
                        vdc=self.cleaned_data.get('vdc'),
                        address=self.cleaned_data.get('address'),)

        seller.save(request)
        # content ={
        #     "seller":seller,
        #     "user": user
        # }
        return user

class SellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Seller
        fields = '__all__'
        # depth = 1

class SellerProfileUpdateSerializer(serializers.ModelSerializer):
    seller = SellerProfileSerializer()
    email = serializers.EmailField(required=False)
    class Meta:
        model = User
        fields = ['id', "first_name", "last_name","email",'seller']
        depth = 1

    def update(self, instance, validated_data):
        user = self.context['request'].user
        user.first_name = validated_data.get('first_name')
        user.last_name = validated_data.get('last_name')
        user.email = validated_data.get('email')
        seller_data = validated_data.pop('seller',None)
        if seller_data is not None:
            instance.seller.business_name = seller_data['business_name']
            instance.seller.phone_num = seller_data['phone_num']
            instance.seller.legal_name = seller_data['legal_name']
            instance.seller.company_registration_name = seller_data['company_registration_name']
            instance.seller.business_registration_no = seller_data['business_registration_no']
            instance.seller.business_email = seller_data['business_email']
            instance.seller.docs = seller_data['docs']
            instance.seller.first_name = seller_data['first_name']
            instance.seller.last_name = seller_data['last_name']
            instance.seller.mob_num = seller_data['mob_num']
            instance.seller.state = seller_data['state']
            instance.seller.district = seller_data['district']
            instance.seller.vdc = seller_data['vdc']
            instance.seller.address = seller_data['address']
            instance.seller.save()
        return super().update(instance,validated_data)




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
                raise serializers.ValidationError("This is not a seller account")

        data['user'] = user

        return data

class CustomerRegisterSerializer(RegisterSerializer):
    customer = serializers.PrimaryKeyRelatedField(read_only=True,)
    phone_num = serializers.CharField(required=False)
    username = None
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    def get_cleaned_data(self):
        data = super(CustomerRegisterSerializer, self).get_cleaned_data()
        extra_data = {
            'phone_num': self.validated_data.get('phone_num', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        }
        data.update(extra_data)
        return data

    def save(self,request,**kwargs):

        user = super(CustomerRegisterSerializer,self).save(request)
        user.is_customer = True
        user.save()
        customer = Customer(customer=user,
                        phone_num=self.cleaned_data.get('phone_num'),
                        first_name=self.cleaned_data.get('first_name'),
                        last_name=self.cleaned_data.get('last_name'),

                        )

        customer.save()
        return user

class CustomerLoginSerializer(serializers.ModelSerializer):
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
            if not user.is_customer:
                raise serializers.ValidationError("This is not a customer account.")

        data['user'] = user

        return data

# class CustomerProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = '__all__'
#         depth = 1
#
#     def update(self, instance, validated_data):
#         instance.full_name= validated_data.get('full_name',instance.full_name)
#         instance.phone_num = validated_data.get('phone_num', instance.phone_num)
#         instance.region = validated_data.get('region',instance.region)
#         instance.city = validated_data.get('city', instance.city)
#         instance.area = validated_data.get('area', instance.area)
#         instance.address = validated_data.get('address', instance.address)
#         instance.save()
#         return instance




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
