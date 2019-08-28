from rest_framework import serializers
from delivery.models import UserBusinessAgreement, BusinessBusinessAgreement, UserProduct, UserAdress, User, Zone, Characteristic, BusinessVehicle, BusinessAddress, Delivery, Service, StoreProduct, Store, Product, Package, Address, Position, Vehicle, DeliveryPerson, Rating, Step, Request, Timespan, Schedule, Contract


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    products = ProductSerializer(
        many=True,
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number',
                  'identifier', 'agreements', 'products', 'addresses', 'vehicles', 'is_email_verified']


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'


class UserAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBusinessAgreement
        fields = '__all__'


class BusinessAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessBusinessAgreement
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['identifier', 'name', 'is_exclusive', 'zone', 'user_agreements', 'business_agreements',
                  'incoming_business_agreements', 'characteristics', 'addresses', 'vehicles', 'employees']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    products = ProductSerializer(
        many=True,
    )

    class Meta:
        model = Store
        fields = ['identifier', 'name', 'zone', 'user_agreements', 'business_agreements',
                  'incoming_business_agreements', 'addresses', 'vehicles', 'employees', 'products']


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        exclude = ['request']


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


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        exclude = ['request']


class RequestSerializer(serializers.ModelSerializer):
    steps = StepSerializer(
        many=True,
        read_only=True
    )

    rating = RatingSerializer(
        read_only=True
    )

    packages = PackageSerializer(
        many=True,
        read_only=True
    )

    #Hacer el handles

    class Meta:
        model = Request
        fields = '__all__'


class TimespanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timespan
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        exclude = ['contract']


class ContractSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Contract
        fields = ['schedule', 'delivery_person', 'business']
