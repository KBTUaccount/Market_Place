from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from orders.models import Order, OrderItem
from products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OrderItem
        fields = ['product_id', 'product_name', 'quantity', 'price_at_purchase']
        read_only_fields = ['id', 'price_at_purchase', 'product_name']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['buyer', 'created_at', 'is_paid', 'items']
        read_only_fields = ['id', 'buyer', 'created_at', 'is_paid']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user

        total_price = 0
        for item in items_data:
            product = Product.objects.get(pk=item['product_id'])
            total_price += product.price * item['quantity']

        if user.balance < total_price:
            raise ValidationError('Not enough balance to complete the purchase.')

        user.balance -= total_price
        user.save()

        order = Order.objects.create(buyer=user)

        for item in items_data:
            product = Product.objects.get(pk=item['product_id'])
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item['quantity'],
                price_at_purchase=product.price
            )

        return order
