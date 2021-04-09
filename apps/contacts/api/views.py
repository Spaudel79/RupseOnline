from ..models import *
from .serializers import AboutUsSerializers,ContactSerializers,RupseSerializers
from rest_framework.generics import (CreateAPIView,ListAPIView)
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.core.mail import send_mail

class AboutUsAPIView(ListAPIView):
    permission_classes =[AllowAny]
    serializer_class = AboutUsSerializers
    queryset = AboutUs.objects.all().order_by('-id')[:1]

class ContactAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        name = serializer.data['full_name']
        email = serializer.data['email']
        phone = serializer.data['phone']
        subject = serializer.data['subject']
        send_mail('New Contact ', f"Rupseonline:Contact has been made by {name} "
                                  f"having email {email} & phone {phone} "
                                  f"and subject '{subject}' ",
                  email, ['info@rupseonline.com', 'shreya.aakashlabs@gmail.com',
                          'ankur.aakashlabs@gmail.com'],
                  fail_silently=False)

class RupseAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = RupseSerializers
    queryset = ContactInfo.objects.all().order_by('-id')[:1]
