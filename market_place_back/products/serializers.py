from rest_framework import serializers
from products.models import Category, Product
from users.models import CustomUser

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category
        
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
    

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'category', 'seller']
        read_only_fields = ['seller', 'id']

