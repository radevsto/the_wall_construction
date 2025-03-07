def test_exceed_high(exceed_section_high):
    expected_msg = "Profile 1 contains section/s higher than the limit of: 2!"
    assert exceed_section_high.message == expected_msg


def test_exceed_section_quantity(exceed_section_quantity):
    expected_msg = "2 of profile 1 is higher than the limit of 1!"
    assert exceed_section_quantity.message == expected_msg
