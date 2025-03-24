from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField



class UserProfile(AbstractUser):
    STATUS_ROLE = (
        ('администратор', 'администратор'),
        ('продавец', 'продавец'),
        ('покупатель', 'покупатель')
    )
    Role = models.CharField(max_length=200, default='покупатель', choices=STATUS_ROLE)
    phone_number = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class Brand(models.Model):
    brand = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return f'{self.brand}'


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return f'{self.model}'



class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    year = models.IntegerField()
    FUEL_TYPE_STATUS = (
        ('бензин', 'бензин'),
        ('дизель', 'дизель'),
        ('Гибридные', 'Гибридные'),
        ('Газообразные', 'Газообразные'),
        ('Электромобили', 'Электромобили')
    )
    fuel_type = models.CharField(max_length=100, default='бензин', choices=FUEL_TYPE_STATUS)
    TRANSMISSION_TYPE = (
        ('Автомат', 'Автомат'),
        ('механика', 'механика')
    )
    transmission_type = models.CharField(max_length=100, default='Автомат', choices=TRANSMISSION_TYPE)
    mileage = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    description = models.TextField()
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand}, {self.model}'


class CarImages(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='cars_images/')



class Auction(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='auction')
    start_price = models.PositiveIntegerField()
    min_price = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    STATUS_ACTIVE = (
        ('активен','активен'),
        ('завершен','завершен'),
        ('отменен','отменен')
    )
    status = models.CharField(max_length=120, default='активен', choices=STATUS_ACTIVE)

    def __str__(self):
        return f'{self.car}, {self.start_price}, {self.start_time}'


class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='auc_bids')
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='bid')
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.auction}, {self.buyer}'



class Feedback(models.Model):
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='seller')
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='buyer')
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()

    def __str__(self):
        return f'Саттуучу {self.seller}, Алуучу {self.buyer}'
