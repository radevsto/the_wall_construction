import pytest
from TheWall.serializers import (
    DaySerializer,
    OverviewSerializer,
    TotalOverviewSerializer,
)


@pytest.mark.django_db
class TestDaySerializer:
    def test_day_serializer_valid_data(self):
        # Arrange
        day_data = {"day_number": 1, "ice_amount": 5, "cost": 100}
        serializer = DaySerializer(data=day_data)
        assert serializer.is_valid()
        assert serializer.validated_data == day_data

    def test_day_serializer_invalid_data(self):
        invalid_day_data = {
            "day_number": None,  # Invalid value
            "ice_amount": 5,
            "cost": 100,
        }
        serializer = DaySerializer(data=invalid_day_data)
        assert not serializer.is_valid()
        assert "day_number" in serializer.errors


@pytest.mark.django_db
class TestOverviewSerializer:
    def test_overview_serializer_valid_data(self):
        overview_data = {"day": 1, "cost": "100"}

        serializer = OverviewSerializer(data=overview_data)
        assert serializer.is_valid()
        assert serializer.validated_data == overview_data

    def test_overview_serializer_invalid_data(self):
        invalid_overview_data = {"day": None, "cost": "100"}  # Invalid value
        serializer = OverviewSerializer(data=invalid_overview_data)
        assert not serializer.is_valid()
        assert "day" in serializer.errors


@pytest.mark.django_db
class TestTotalOverviewSerializer:
    def test_total_overview_serializer_valid_data(self):
        total_overview_data = {"day": "1", "cost": "100"}
        serializer = TotalOverviewSerializer(data=total_overview_data)
        assert serializer.is_valid()
        assert serializer.validated_data == total_overview_data

    def test_total_overview_serializer_invalid_data(self):
        invalid_total_overview_data = {"cost": None}
        serializer = TotalOverviewSerializer(data=invalid_total_overview_data)
        assert not serializer.is_valid()
        assert "cost" in serializer.errors
