from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Product, Cart, CartItem, Order, OrderItem
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, ProductSerializer, CartItemSerializer, OrderSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['POST'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            print("yahan fasa")
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def get_cart(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def add_to_cart(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        cart, created = Cart.objects.get_or_create(user=request.user)
        product = Product.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()

        return Response({'message': 'Product added to cart'}, status=status.HTTP_200_OK)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)

        if not cart_items:
            return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

        total_price = sum(item.product.price * item.quantity for item in cart_items)
        order = Order.objects.create(user=request.user, total_price=total_price)

        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price
            )

        cart_items.delete()

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)