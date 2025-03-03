from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartItemViewSet, CartViewSet

# Crear un router per a la vista de Cart i CartItem
router = DefaultRouter()
router.register(r'cart-items', CartItemViewSet)
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
]
