from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["id","name","year","user_id"]
        read_only_fields = ["id", "user_id"]

    def create(self, validated_data):
        return Album.objects.create(**validated_data)


# old serializers
class AlbumSerializerOld(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    year = serializers.IntegerField()
    user_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Album.objects.create(**validated_data)