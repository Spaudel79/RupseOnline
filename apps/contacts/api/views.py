from ..models import *
from .serializers import AboutUsSerializers,ContactSerializers,RupseSerializers
from rest_framework.generics import (CreateAPIView,ListAPIView)
from rest_framework.permissions import AllowAny,IsAuthenticated


class AboutUsAPIView(ListAPIView):
    permission_classes =[AllowAny]
    serializer_class = AboutUsSerializers
    queryset = AboutUs.objects.all().order_by('-id')[:1]

class ContactAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()

class RupseAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = RupseSerializers
    queryset = ContactInfo.objects.all().order_by('-id')[:1]
