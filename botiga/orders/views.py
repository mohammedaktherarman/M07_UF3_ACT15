from rest_framework import viewsets
from .models import Order, OrderItem
from .serializers import OrderSerializer


def checkout_cart(cart):
    order = Order.objects.create(user=cart.user, total_price=calculate_total(cart))

    for item in cart.items.all():
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)

    cart.items.all().delete()
    return order

def calculate_total(cart):
    total = 0
    for item in cart.items.all():
        total += item.product.price * item.quantity
    return total

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
