from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

# Crear un router per a la vista de Order
router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    # Incloure les rutes creades pel router
    path('', include(router.urls)),
]
