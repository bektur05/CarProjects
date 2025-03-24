from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'first_name', 'last_name', 'Role', 'phone_number']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'brand']


class ModelSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)

    class Meta:
        model = Model
        fields = ['id', 'brand', 'model']


class CarSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    model = ModelSerializer(read_only=True)
    seller = UserProfileSerializer()

    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'year', 'fuel_type',
                  'transmission_type', 'mileage', 'price', 'description', 'seller']


class CarImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImages
        fields = ['id', 'car', 'images']


class AuctionSerializer(serializers.ModelSerializer):
    car = CarSerializer()

    class Meta:
        model = Auction
        fields = ['id', 'car', 'start_price', 'min_price',
                  'start_time', 'end_time', 'status']


class BidSerializer(serializers.ModelSerializer):
    auction = AuctionSerializer()
    buyer = UserProfileSerializer()

    class Meta:
        model = Bid
        fields = ['id', 'auction', 'buyer', 'amount', 'created_at']


class FeedbackSerializer(serializers.ModelSerializer):
    seller = UserProfileSerializer(read_only=True)
    buyer = UserProfileSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = ['id', 'seller', 'buyer',  'comment']