from rest_framework import serializers


class CreateAccountSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
