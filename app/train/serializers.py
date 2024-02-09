from rest_framework import serializers
from .models import TrainUser, Station, Train, Stop

class TrainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainUser
        fields = '__all__'

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'


class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = ['station_id', 'arrival_time', 'departure_time', 'fare']

class TrainSerializer(serializers.ModelSerializer):
    stops = StopSerializer(many=True)

    class Meta:
        model = Train
        fields = ['train_id', 'train_name', 'capacity', 'stops']
    
    def create(self, validated_data):
        stops_data = validated_data.pop('stops')
        train = Train.objects.create(**validated_data)
        for stop_data in stops_data:
            Stop.objects.create(train=train, **stop_data)
        return train

# # class RecipeSerializer(serializers.ModelSerializer):
#     """Serialize a recipe"""
#     ingredients = serializers.PrimaryKeyRelatedField(
#         many=True,
#         queryset=Ingredient.objects.all()
#     )
#     tags = serializers.PrimaryKeyRelatedField(
#         many=True,
#         queryset=Tag.objects.all()
#     )

#     class Meta:
#         model = Train
#         fields = (
#             'id', 'title', 'ingredients', 'tags', 'time_minutes',
#             'price', 'link'
#         )
#         read_only_fields = ('id',)

