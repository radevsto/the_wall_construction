import os
import pytest
import logging
import tempfile
from dataclasses import dataclass
from TheWall.custom_exceptions import ExceededHighOfSections, ExceededNumberOfSections
from TheWall.utilities import ConfigReader, setup_logger
from TheWall.construction_management import Crew, Section
from TheWall.construction_manager import ConstructionManager as BranTheBuilder


@pytest.fixture()
def cfg_file():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        content = "21 22 23\n24 25\n26"
        temp_file.write(content.encode("utf8"))

    yield temp_file.name
    os.remove(temp_file.name)


@pytest.fixture()
def cfg_reader_instance(cfg_file):
    return ConfigReader(cfg_file)


@pytest.fixture()
def exceed_section_high():
    return ExceededHighOfSections(2, 1)


@pytest.fixture()
def exceed_section_quantity():
    return ExceededNumberOfSections(2, 1, 1)


@pytest.fixture()
def crew():
    return Crew(number=1, section_height=15)


@pytest.fixture()
def crew_max_height():
    return Crew(number=1, section_height=30)


@dataclass
class DummyCrew:
    number: int
    busy: bool = True


@pytest.fixture
def setup_section():
    crews = [DummyCrew(n) for n in range(5)]
    all_crews = []
    section = Section(crews=crews, all_crews=all_crews, height=0, profile_id=1)
    return section, crews, all_crews


@pytest.fixture
def setup_section_complete():
    crews = [DummyCrew(n) for n in range(5)]
    all_crews = []
    section = Section(crews=crews, all_crews=all_crews, height=30, profile_id=1)
    return section, crews, all_crews


@pytest.fixture
def construction_manager(cfg_file):
    manager = BranTheBuilder(construction_doc=cfg_file)
    return manager


@pytest.fixture()
def logger_setup():
    logger = setup_logger('TestLogger', log_file='application.log', level=logging.DEBUG)
    yield logger
    # Cleanup after test
    for handler in logger.handlers:
        handler.close()
        logger.removeHandler(handler)
