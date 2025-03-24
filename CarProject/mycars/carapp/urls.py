
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'models', ModelViewSet)
router.register(r'cars', CarViewSet)
router.register(r'car-images', CarImagesViewSet)
router.register(r'auctions', AuctionViewSet)
router.register(r'bids', BidViewSet)
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]