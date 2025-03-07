from rest_framework import serializers
from .models import Day


class DaySerializer(serializers.ModelSerializer):
    """
    Serializer for the Day model.

    This serializer is used to serialize and deserialize Day instances.

    Attributes:
        day_number (int): The day number associated with the Day instance.
        ice_amount (int): The amount of ice associated with the Day instance.
        cost (int): The cost associated with the Day instance.
    """

    class Meta:
        model = Day
        fields = ["day_number", "ice_amount", "cost"]


class OverviewSerializer(serializers.Serializer):
    """
    Serializer for providing an overview of a day's cost.

    This serializer is used to represent minimal information about a day's cost,
    specifically for API endpoints that return summaries of costs per day.

    Attributes:
        day (int): The day number.
        cost (int): The cost associated with that day, formatted as a string.
    """

    day = serializers.IntegerField()
    cost = serializers.CharField()


class TotalOverviewSerializer(serializers.Serializer):
    """
    Serializer for providing total overview cost information.

    This serializer represents the total cost overview and can be used for
    API endpoints that return financial summaries for all days or profiles.

    Attributes:
        day (str): The day number, default is None if not applicable.
        cost (str): The total cost associated with the day or profile.
    """

    day = serializers.CharField(default=None)
    cost = serializers.CharField()
