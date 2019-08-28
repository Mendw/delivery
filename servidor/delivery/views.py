# pylint: disable=no-member

from delivery.models import *
from delivery.serializers import *
from rest_framework import generics


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# ========================================= #


class ZoneList(generics.ListCreateAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer


class ZoneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
# ========================================= #


class CharacteristicList(generics.ListCreateAPIView):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer


class CharacteristicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer
# ========================================= #


class DeliveryList(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class DeliveryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
# ========================================= #


class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
# ========================================= #


class DeliveryPersonList(generics.ListCreateAPIView):
    queryset = DeliveryPerson.objects.all()
    serializer_class = DeliveryPersonSerializer


class DeliveryPersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeliveryPerson.objects.all()
    serializer_class = DeliveryPersonSerializer
# ========================================= #

