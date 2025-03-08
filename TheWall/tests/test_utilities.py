import copy
import pytest
from TheWall.custom_exceptions import ExceededHighOfSections, ExceededNumberOfSections


def test_get_data_valid(cfg_reader_instance):
    """Test that get_data returns the expected parsed data."""
    expected_data = [[21, 22, 23], [24, 25], [26]]
    assert cfg_reader_instance.get_data() == expected_data


def test_get_data_exceeds_sections(cfg_reader_instance):
    """Test that ExceededNumberOfSections is raised for too many sections."""
    cfg_r_instance = copy.deepcopy(cfg_reader_instance)
    cfg_r_instance.max_number_of_sections = 1
    with pytest.raises(ExceededNumberOfSections) as e:
        cfg_r_instance.get_data()
    assert "higher than the limit" in str(e.value)


def test_get_data_exceeds_section_height(cfg_reader_instance):
    """Test that ExceededHighOfSections is raised for excessive heights."""
    cfg_r_instance = copy.deepcopy(cfg_reader_instance)
    cfg_r_instance.required_section_high = 1
    with pytest.raises(ExceededHighOfSections) as e:
        cfg_r_instance.get_data()
    assert "contains section/s higher than the limit" in str(e.value)


def test_file_not_found(cfg_reader_instance):
    """Test that FileNotFoundError is raised for a missing file."""
    cfg_reader_instance.input_file = "non_existent_file.txt"
    with pytest.raises(FileNotFoundError) as e:
        cfg_reader_instance.get_data()

    assert "Input file missing:" in str(e.value)
