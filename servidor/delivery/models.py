from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    phone_number = models.CharField(max_length=31, null=True, default=None, blank=True)
    identifier = models.CharField(max_length=20, unique=True, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)


class Zone(models.Model):
    name = models.CharField(max_length=20)
    query = models.TextField()
    placeID = models.TextField()


class Characteristic(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    icon = models.ImageField()


class Business(models.Model):
    identifier = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True)
    user_agreements = models.ManyToManyField(User, through='UserBusinessAgreement', related_name='agreements')
    business_agreements = models.ManyToManyField('Business', through='BusinessBusinessAgreement')


class Delivery(Business):
    is_exclusive = models.BooleanField()
    characteristics = models.ManyToManyField(Characteristic)


class Service(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    pickup_time = models.TimeField()
    delivery_time = models.TimeField()
    max_weight = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True)
    max_heigth = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True)
    max_length = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True)
    max_width = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        validators=[MinValueValidator(0)],
        blank=True,
        null=True)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)


class Store(Business):
    pass


class Product(models.Model):
    identifier = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    decription = models.TextField()


class StoreProduct(Product):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')


class UserProduct(Product):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')


class Treatment(models.Model):
    icon = models.ImageField()
    name = models.CharField(max_length=30)
    description = models.TextField()


class Package(models.Model):
    request = models.ForeignKey('Request', on_delete=models.CASCADE, null=True, related_name='packages')
    identifier = models.CharField(max_length=30)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.DecimalField(max_digits=4, decimal_places=2)
    treatments = models.ManyToManyField(Treatment)
    products = models.ManyToManyField(Product)

class Address(models.Model):
    coordinates = models.CharField(max_length=30, null=True)
    title = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=31)
    instructions = models.TextField(null=True)


class Position(models.Model):
    coordinates = models.CharField(max_length=30, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True)


class Status(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()


class VehicleType(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.PROTECT)
    color = models.CharField(max_length=30)
    license_plate = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    make = models.CharField(max_length=30)
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2050)])
    photo = models.ImageField(null=True)


class UserVehicle(Vehicle):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicles')


class BusinessVehicle(Vehicle):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='vehicles')


class BusinessAddress(Address):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='addresses')


class UserAdress(Address):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')


class DeliveryPerson(User):
    is_SMS_active = models.BooleanField()
    is_freelancer = models.BooleanField()
    is_verified = models.BooleanField()
    is_working = models.BooleanField()
    worksFor = models.ManyToManyField(
        Business,
        through='Contract',
        related_name='employees'
    )


class Request(models.Model):
    identifier = models.CharField(max_length=30)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    postition = models.OneToOneField(Position, on_delete=models.PROTECT)
    delivery_person = models.ForeignKey(
        DeliveryPerson, on_delete=models.SET_NULL, null=True)
    delivery_company = models.ForeignKey(
        Delivery, on_delete=models.CASCADE
    )
    handled_by = models.OneToOneField(
        'Request', on_delete=models.PROTECT, null=True, related_name='handles'
    )


class Step(models.Model):
    is_done = models.BooleanField()
    description = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='steps')


class Rating(models.Model):
    score = models.PositiveIntegerField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    request = models.OneToOneField(Request, on_delete=models.CASCADE)


class Day(models.Model):
    name = models.CharField(max_length=12)


class Timespan(models.Model):
    day = models.ForeignKey(Day, on_delete=models.PROTECT)
    start = models.TimeField()
    end = models.TimeField()


class Contract(models.Model):
    delivery_person = models.ForeignKey(
        DeliveryPerson,
        on_delete=models.CASCADE
    )
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE
    )


class Schedule(Timespan):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='schedule')


class UserBusinessAgreement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    is_accepted = models.BooleanField()


class BusinessBusinessAgreement(models.Model):
    source = models.ForeignKey(Business, on_delete=models.CASCADE)
    target = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='incoming_business_agreements')
    description = models.TextField(blank=True)
    is_accepted = models.BooleanField()


class Note(models.Model):
    identifier = models.BigIntegerField(validators=[MinValueValidator(0)])
    title = models.CharField(max_length=50)
    description = models.TextField()
    priority = models.PositiveIntegerField()