import pytest
from unittest.mock import MagicMock, patch
from TheWall.models import Profile, Day
from TheWall.construction_management import Crew, Section


def test_crew_methods(construction_manager):
    construction_manager._get_construction_parameters()
    assert construction_manager.construction_parameters == [
        [21, 22, 23],
        [24, 25],
        [26],
    ]
    crews = construction_manager._assemble_crews()
    assert len(crews) == 6
    assert all(isinstance(crew, Crew) for crew in crews)
    construction_manager._setup_crews()
    assert len(construction_manager.sections) == len(
        sum(construction_manager.construction_parameters, [])
    )
    assert all(
        isinstance(section, Section) for section in construction_manager.sections
    )
    construction_manager.crews.extend([Crew(n, 15) for n in range(7, 10)])
    construction_manager._spread_crews(construction_manager.sections)
    assert not construction_manager.crews
    assert len(construction_manager.sections[0].crews) == 2
    assert len(construction_manager.sections[1].crews) == 2
    assert len(construction_manager.sections[2].crews) == 2


@patch.object(Profile, "save", MagicMock(name="save"))
def test_create_profile_entries(construction_manager):
    construction_manager._setup_crews()
    construction_manager._create_profile_entries()
    assert Profile.save.call_count == len(construction_manager.construction_parameters)


@pytest.mark.django_db
def test_write_day_entry(construction_manager):
    profile = Profile(name=1000)
    profile.save()
    construction_manager._write_day_entry(profile_id=1000, day=1, cost=100.00, ice=10)
    day_entry = Day.objects.get(day_number=1, profile=profile)
    assert day_entry.cost == 100.00
    assert day_entry.ice_amount == 10
    assert day_entry.profile == profile
