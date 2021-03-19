from ..models import *
from rest_framework import serializers

class AboutUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'
        depth = 1

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class RupseSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'