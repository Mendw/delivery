from rest_framework import serializers
from delivery.models import *


class UserSerializer(serializers.ModelSerializer):
    agreements = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Agreement.objects.all()  # pylint: disable=no-member
    )
    products = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=UserProduct.objects.all()  # pylint: disable=no-member
    )

    addresses = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=UserAdress.objects.all()  # pylint: disable=no-member
    )

    addresses = serializers.PrimaryKeyRelatedField

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'phone_number', 'identifier', 'agreements', 'products', 'is_email_verified']


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    vehicles = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=BusinessVehicle.objects.all()  # pylint: disable=no-member
    )

    addresses = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=BusinessAddress.objects.all()  # pylint: disable=no-member
    )

    class Meta:
        model = Delivery
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=StoreProduct.objects.all()  # pylint: disable=no-member
    )

    vehicles = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=BusinessVehicle.objects.all()  # pylint: disable=no-member
    )

    addresses = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=BusinessAddress.objects.all()  # pylint: disable=no-member
    )

    class Meta:
        model = Store
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class DeliveryPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPerson
        fields = ['username', 'first_name', 'last_name',
                  'email', 'phone_number', 'identifier',
                  'agreements', 'products', 'is_email_verified',
                  'is_SMS_active', 'is_freelancer', 'is_verified',
                  'is_working', 'worksFor']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        exclude = ['request']


class RequestSerializer(serializers.ModelSerializer):
    steps = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Step.objects.all()  # pylint: disable=no-member
    )
    packages = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Package.objects.all()  # pylint: disable=no-member
    )

    rating = RatingSerializer()

    class Meta:
        model = Request
        fields = '__all__'


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'

class TimespanSerializer(serializers.ModelSerializer):
    pass

class ContractSerializer(serializers.ModelSerializer):
    pass

class ScheduleSerializer(serializers.ModelSerializer):
    pass

class AgreementSerializer(serializers.ModelSerializer):
    pass