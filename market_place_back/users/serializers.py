from rest_framework import serializers
from users.models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)
    balance = serializers.DecimalField(max_digits=10, decimal_places=2, default=0)

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username = validated_data['username'],
            balance = validated_data['balance']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.balance = validated_data.get('balance', instance.balance)
        if 'password' in validated_data:
            instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance