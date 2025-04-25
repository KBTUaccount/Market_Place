from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from orders.models import Order
from orders.serializers import OrderSerializer
from products.models import Product
from products.serializers import ProductSerializer
from users.models import CustomUser
from users.serializers import CustomUserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


@api_view(['GET'])
def profile(request):
    user = request.user

    user_products = Product.objects.filter(seller=user)
    user_orders = Order.objects.filter(buyer=user)

    products_data = ProductSerializer(user_products, many=True).data
    orders_data = OrderSerializer(user_orders, many=True).data

    return Response({
        "username": user.username,
        "balance": user.balance,
        "products": products_data,
        "orders": orders_data
    })


