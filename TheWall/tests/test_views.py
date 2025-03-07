import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from TheWall.models import Day, Profile


@pytest.mark.django_db
class TestViews:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.profile = Profile.objects.create(name=1)
        self.day1 = Day.objects.create(
            profile=self.profile, day_number=1, cost=100, ice_amount=10
        )
        self.day2 = Day.objects.create(
            profile=self.profile, day_number=2, cost=200, ice_amount=20
        )

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        assert response.status_code == status.HTTP_200_OK
        assert "index.html" in response.templates[0].name

    def test_profile_on_day_ice(self):
        response = self.client.get(
            reverse(
                "profile-on-day-ice-amount",
                args=[self.profile.id, self.day1.day_number],
            )
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["day"] == str(self.day1.day_number)
        assert response.data["ice_amount"] == str(self.day1.ice_amount)

    def test_profile_on_day_cost(self):
        response = self.client.get(
            reverse("profile-on-day-cost", args=[self.profile.id, self.day1.day_number])
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["day"] == self.day1.day_number
        assert response.data["cost"] == f"{self.day1.cost}"

    def test_day_overview(self):
        response = self.client.get(
            reverse("day-overall-cost", args=[self.day1.day_number])
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["day"] == self.day1.day_number
        assert response.data["cost"] == f"{self.day1.cost}"

    def test_profile_overview(self):
        response = self.client.get(
            reverse("profile-overall-cost", args=[self.profile.id])
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["day"] is None
        assert response.data["cost"] == f"{self.day1.cost + self.day2.cost}"

    def test_total_cost_overview(self):
        response = self.client.get(reverse("total-cost-overview"))
        assert response.status_code == status.HTTP_200_OK
        assert response.data["cost"] == f"{self.day1.cost + self.day2.cost}"
