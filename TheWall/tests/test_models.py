import pytest
from TheWall.models import Profile, Day
from django.db import IntegrityError


@pytest.mark.django_db
class TestProfileModel:
    def test_profile_string_representation(self):
        """Test the string representation of a Profile object."""
        profile = Profile.objects.create(name=1000)
        assert str(profile) == "1000"


@pytest.mark.django_db
class TestDayModel:
    def test_day_string_representation(self):
        """Test the string representation of a Day object."""
        profile = Profile.objects.create(name=1000)
        day = Day.objects.create(profile=profile, day_number=1, cost=100, ice_amount=10)

        assert str(day) == "Day 1 for 1000"

    def test_unique_together_constraint(self):
        """Test unique together constraint on Day model."""
        profile = Profile.objects.create(name=1)
        Day.objects.create(profile=profile, day_number=1, cost=100, ice_amount=10)

        assert Day.objects.count() == 1

        with pytest.raises(IntegrityError) as e:
            Day.objects.create(profile=profile, day_number=1, cost=200, ice_amount=30)

        assert "UNIQUE constraint failed" in str(e.value)
