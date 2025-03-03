from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartItemSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def create(self, request, *args, **kwargs):
        cart = Cart.objects.get(user=request.user)
        product_id = request.data.get("product")
        quantity = request.data.get("quantity", 1)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product_id=product_id, defaults={"quantity": quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        return Response(CartItemSerializer(cart_item).data, status=status.HTTP_201_CREATED)

class CartViewSet(viewsets.ViewSet):
    def list(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        serialized_items = CartItemSerializer(cart_items, many=True)
        return Response(serialized_items.data)
