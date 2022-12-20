from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
        "id",
        "username",
        "email",
        "password",
        "first_name",
        "last_name",
        "is_superuser",
        ]
        extra_kwargs = {
                "email": {
                    "validators": [UniqueValidator(User.objects.all())]
                },
                "username":{
                    "validators": [UniqueValidator(User.objects.all(),"A user with that username already exists.")]
                },
                "is_superuser":{"read_only": True},

                "password": {"write_only": True},

        }

    def create(self, validated_data: dict) -> User:

        return User.objects.create_superuser(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
