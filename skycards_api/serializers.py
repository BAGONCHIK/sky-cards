from rest_framework import serializers

from skycards_api.models import Card


class CreateCardSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    bg_number = serializers.CharField(max_length=255)

    class Meta:
        model = Card
        fields = ['email', 'text', 'place', 'time', 'bg_number']


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'text', 'place', 'time', 'card_url', 'bg_url']
