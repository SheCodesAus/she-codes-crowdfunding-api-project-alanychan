from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']
        read_only_fields = ['id']
        extra_kwargs = {"password":{"write_only":True}}

    # id = serializers.ReadOnlyField()
    # username = serializers.CharField(max_length=150)
    # email = serializers.EmailField()

    def create(self, validated_data):
        user = CustomUser.objects.create(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)

        if password := validated_data.get('password'):
            instance.set_password(password)

        instance.save()

        return instance

