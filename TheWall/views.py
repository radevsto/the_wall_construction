from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Day
from .serializers import DaySerializer, OverviewSerializer, TotalOverviewSerializer


def home(request):
    """
    Render the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered 'index.html' template.
    """
    return render(request, "index.html")


class ProfileOnDayIce(APIView):
    """
    API view to retrieve ice amount for a specific profile on a specific day.
    """

    def get(self, request, profile_id, day_number):
        """
        Handle GET request to return the ice amount for a specific profile and day.

        Args:
            request: The HTTP request object.
            profile_id: The ID of the profile.
            day_number: The day number for which to retrieve the ice amount.

        Returns:
            Response: A response containing the day number and ice amount.
        """
        day = Day.objects.get(profile__id=profile_id, day_number=day_number)
        serializer = DaySerializer(day)
        return Response(
            {
                "day": str(day.day_number),
                "ice_amount": str(serializer.data["ice_amount"]),
            }
        )


class ProfileOnDayCost(APIView):
    """
    API view to retrieve cost for a specific profile on a specific day.
    """

    def get(self, request, profile_id, day_number):
        """
        Handle GET request to return the cost for a specific profile and day.

        Args:
            request: The HTTP request object.
            profile_id: The ID of the profile.
            day_number: The day number for which to retrieve the cost.

        Returns:
            Response: A response containing the day number and cost.
        """
        day = Day.objects.get(profile__id=profile_id, day_number=day_number)
        serializer = OverviewSerializer(
            {"day": day.day_number, "cost": f"{day.cost:,}"}
        )
        return Response(serializer.data)


class DayOverview(APIView):
    """
    API view to get an overview of a specific day including total cost.
    """

    def get(self, request, day_number):
        """
        Handle GET request to return total cost for a specific day.

        Args:
            request: The HTTP request object.
            day_number: The day number for which to retrieve the overview.

        Returns:
            Response: A response containing the day number and total cost.
        """
        days = Day.objects.filter(day_number=day_number)
        total_cost = sum(day.cost for day in days)
        serializer = OverviewSerializer(
            {
                "day": days.first().day_number if days.exists() else None,
                "cost": f"{total_cost:,}",
            }
        )
        return Response(serializer.data)


class ProfileOverview(APIView):
    """
    API view to get an overview of costs for all days under a specific profile.
    """

    def get(self, request, profile_id):
        """
        Handle GET request to return total cost for all days related to a specific profile.

        Args:
            request: The HTTP request object.
            profile_id: The ID of the profile.

        Returns:
            Response: A response containing the total cost for the profile.
        """
        days = Day.objects.filter(profile__id=profile_id)
        total_cost = sum(day.cost for day in days)
        serializer = OverviewSerializer({"day": None, "cost": f"{total_cost:,}"})
        return Response(serializer.data)


class TotalCostOverview(APIView):
    """
    API view to get the total cost overview for all days.
    """

    def get(self, request):
        """
        Handle GET request to return the total cost across all days.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A response containing the total cost.
        """
        total_cost = sum(day.cost for day in Day.objects.all())
        serializer = TotalOverviewSerializer({"cost": f"{total_cost:,}"})
        return Response(serializer.data)
