# pylint: disable=no-member

from delivery.models import *
from delivery.serializers import *

from django.contrib.auth.forms import UserCreationForm
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
from django.contrib.auth import login

from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from django.shortcuts import render, redirect


class Registration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        user.email_user('Activate your -El Menu- account', render_to_string(
            'confirmation-email.html', {
                'user': user,
                'domain': get_current_site(request).domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            }
        ))

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.is_email_verified = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserOverviewSerializer


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


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
