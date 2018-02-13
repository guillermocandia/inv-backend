from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        fields = ('id', 'username', 'last_login', 'is_superuser',
                  'first_name', 'last_name', 'email',
                  'is_staff', 'is_active', 'date_joined')
#  TODO definir readonly


class UserPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=False)
    password_new = serializers.CharField()
