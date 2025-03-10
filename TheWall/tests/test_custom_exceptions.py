def test_exceed_height(exceed_section_height):
    expected_msg = "Profile 1 contains section/s higher than the limit of: 2!"
    assert exceed_section_height.message == expected_msg


def test_exceed_section_quantity(exceed_section_quantity):
    expected_msg = "2 of profile 1 is higher than the limit of 1!"
    assert exceed_section_quantity.message == expected_msg
