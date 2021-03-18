from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager with email as the unique identifier
    """

    def create_user(self, first_name, last_name, email, password, **extra_fields):
        """
        Create user with the given email and password.
        """
        if not email:
            raise ValueError("The email must be set")
        first_name = first_name.capitalize()
        last_name = last_name.capitalize()
        email = self.normalize_email(email)

        user = self.model(
            first_name=first_name, last_name=last_name, email=email, **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        """
        Create superuser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(first_name, last_name, email, password, **extra_fields)

# class UserType(models.Model):
#     Customer = 1
#     Vendor = 2
#     Admin = 3
#     Type_Choices = (
#         (Customer, 'Customer'),
#         (Vendor, 'Vendor'),
#         (Admin, 'Admin'),
#     )

class CustomUser(AbstractUser):
    # username = None
    first_name = models.CharField(max_length=255, verbose_name="First name")
    last_name = models.CharField(max_length=255, verbose_name="Last name")
    email = models.EmailField(unique=True)

    # Type_Choices = (
    #             (1, 'Customer'),
    #             (2, 'Vendor'),
    #             (3, 'Admin'),
    #         )
    # user_type = models.IntegerField(choices=Type_Choices, default=1)

    is_seller = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Seller(models.Model):
    seller = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    business_name = models.CharField(max_length=50, blank=True)
    phone_num = models.CharField(max_length=50, blank=True)
    legal_name = models.CharField(max_length=50, blank=True)
    company_registration_name = models.CharField(max_length=50, blank=True)
    business_registration_no = models.CharField(max_length=50, blank=True)
    business_email = models.EmailField()
    docs = models.FileField(blank=True, null=True)
    #full_name = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    mob_num = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=50, blank=True)
    vdc = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.seller.email


class Customer(models.Model):
    customer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    #full_name = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_num = models.CharField(max_length=50, blank=True)
    #dob = models.CharField(max_length=255,blank=True,null=True)
    region = models.CharField(max_length=255, blank=True,null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    area = models.CharField(max_length=255,blank=True,null=True)
    address = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.customer.email
