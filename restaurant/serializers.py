from rest_framework import serializers
from .models import Menu, Booking
from django.contrib.auth.models import User

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class MenuSerializer(serializers.Serializer):
    class Meta:
        model = Menu
        fields = ["id", "title", "price", "inventory"]
