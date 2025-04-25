from rest_framework import generics, permissions

from orders.models import Order
from orders.serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(buyer=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)  # 👈 print the real problem
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)
