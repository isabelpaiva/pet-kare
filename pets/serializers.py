from rest_framework import serializers
from groups.serializers import GroupsSerializer
from traits.serializers import TraitsSerializer
from pets.models import PetChoices


class PetsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(choices=PetChoices.choices, default=PetChoices.DEFAULT)
    group = GroupsSerializer()
    traits = TraitsSerializer(many=True)
