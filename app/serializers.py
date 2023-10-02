from rest_framework import serializers
from .models import Players, Rewards

class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = ['name', 'number']

class RewardsSerializer(serializers.ModelSerializer):
    player = PlayersSerializer()

    class Meta:
        model = Rewards
        fields = ['player']