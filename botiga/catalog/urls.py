from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('catalog/', include(router.urls)),
]