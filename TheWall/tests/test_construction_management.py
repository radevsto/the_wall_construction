def test_crew(crew):
    assert isinstance(crew.number, int)
    assert crew.number == 1
    assert isinstance(crew.section_height, int)
    assert crew.section_height == 15
    assert isinstance(crew.busy, bool)
    assert crew.busy


def test_crew_max_hight(crew_max_height):
    assert isinstance(crew_max_height.number, int)
    assert crew_max_height.number == 1
    assert isinstance(crew_max_height.section_height, int)
    assert crew_max_height.section_height == 30
    assert isinstance(crew_max_height.busy, bool)
    assert not crew_max_height.busy


def test_initialization(setup_section):
    section, crews, all_crews = setup_section
    assert section.height == 0
    assert section.complete is False
    assert section.initial_height == 0
    assert len(all_crews) == 0
    assert len(crews) == len(section.crews)


def test_initialization_complete_section(setup_section_complete):
    section, crews, all_crews = setup_section_complete
    assert section.height == 30
    assert section.complete is True
    assert section.initial_height == 30
    assert len(all_crews) == 5
    assert len(section.crews) == 0


def test_build_without_enough_height(setup_section):
    section, _, _ = setup_section
    section.build()
    assert section.complete is False
    assert section.height == 5


def test_build_with_exact_height(setup_section):
    section, _, all_crews = setup_section
    section.height = 30
    section.build()
    assert section.complete is True
    assert len(all_crews) == 5


def test_build_exceeding_required_height(setup_section):
    section, _, all_crews = setup_section
    section.height = 25
    section.build()
    assert section.complete is True
    assert section.height == 30
    assert len(all_crews) == 5


def test_release_crew(setup_section):
    section, _, all_crews = setup_section
    section._release_crew(2)
    assert all_crews[0].busy is False
    assert all_crews[1].busy is False
    assert len(all_crews) == 2
    assert len(section.crews) == 3
