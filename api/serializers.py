from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import Ad
from rest_framework import serializers


class AdSerializer(ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    phone_number = serializers.IntegerField()

    def validate_true_int(self, value):
        value = self.initial_data.get('phone_number')
        if isinstance(value, int):
            return value
        raise ValidationError("Not an int")

    class Meta:
        model = Ad
        fields = "__all__"