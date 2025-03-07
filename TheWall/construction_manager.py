import os
from itertools import cycle
from concurrent.futures import ThreadPoolExecutor
from .construction_management import Crew, Section
from .utilities import ConfigReader, logger
from .models import Profile, Day

DEFAULT_CFG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")


class ConstructionManager:
    """
    The construction manager of "The Wall" a.k.a. Bran the Builder! :)

    This class handles the organization of construction crews, the processing
    of construction parameters, and the cost calculations associated
    with the building process.

    Attributes:
        cubics_ice_per_section (int): The volume of ice required per section.
        price_per_cubic_ice (int): The cost per cubic unit of ice.
        requires_section_height (int): The height requirement for each section.
        construction_doc (str): The path to the construction configuration file.
        construction_parameters (list[list[int]]): The configuration for construction.
        crews (list[Crew]): The list of construction crews.
        sections (list[Section]): The list of sections to be constructed.
    """

    cubics_ice_per_section = 195
    price_per_cubic_ice = 1900
    requires_section_height = 30

    def __init__(self, construction_doc: str = DEFAULT_CFG) -> None:
        """
        Initialize the ConstructionManager with a configuration document.

        Args:
            construction_doc (str): The path to the input file containing construction parameters.
        """
        self.construction_doc: str = construction_doc
        self.construction_parameters: list[list[int]] = None
        self.crews: list[Crew] = None
        self.sections: list[Section] = list()

    def _get_construction_parameters(self) -> None:
        """
        Load construction parameters from the specified configuration file.

        This method uses the ConfigReader to retrieve the construction parameters
        that will be used to set up crews and sections for the construction.
        """
        cfg_reader = ConfigReader(self.construction_doc)
        self.construction_parameters = cfg_reader.get_data()
        logger.info(f"Obtained construction parameters from {self.construction_doc}")

    def _assemble_crews(self) -> list[Crew]:
        """
        Assemble construction crews based on the loaded construction parameters.

        Returns:
            list[Crew]: A list of Crew instances assembled from the construction parameters.
        """
        self._get_construction_parameters()
        logger.info(f"Construction parameters:\n{self.construction_parameters}")
        combined_sections = sum(self.construction_parameters, [])
        logger.info(f"Overall number of sections: {combined_sections}")
        return [Crew(number, heigh) for number, heigh in enumerate(combined_sections)]

    def _setup_crews(self) -> list[Section]:
        """
        Set up the crews and corresponding sections for construction.

        This method populates the sections list with Section instances,
        each associated with a profile and transferring a crew member to each section.
        """
        self.crews = self._assemble_crews()
        logger.info(f"Hired construction crews: {self.crews}")
        for num, profile in enumerate(self.construction_parameters, 1):
            for section in profile:
                self.sections.append(
                    Section(
                        crews=[self.crews.pop()],
                        height=section,
                        profile_id=num,
                        all_crews=self.crews,
                    )
                )
        logger.info(f"Created sections: {len(self.sections)}")
        for section in self.sections:
            logger.info(section)

    def _spread_crews(self, section_in_progress: list[Section]) -> None:
        """
        Distribute the available crews among sections that are currently being constructed.

        Args:
            section_in_progress (list[Section]): The list of sections that are in the process of being built.
        """
        sorted_sections = cycle(
            sorted(section_in_progress, key=lambda section: section.height)
        )
        for _ in range(len(self.crews)):
            section = next(sorted_sections)
            crew = self.crews.pop()
            logger.info(f"{crew} assigned to {section}")
            crew.busy = True
            section.crews.append(crew)

    def build_the_wall(self) -> None:
        """
        Manage the overall building process for The Wall.

        This method orchestrates the setup of crews, the daily building process,
        and the cost calculations involved for each day until the target height
        is reached for all sections.
        """
        self._setup_crews()
        self._create_profile_entries()
        for day in range(1, self.requires_section_height + 1):
            logger.info(f"Day {day} started:")
            sections_in_progress = [
                section for section in self.sections if not section.complete
            ]
            if len(sections_in_progress):
                logger.info(
                    f"Initiating build for {len(sections_in_progress)} sections."
                )
                self._spread_crews(sections_in_progress)
                with ThreadPoolExecutor(
                    max_workers=len(sections_in_progress)
                ) as executor:
                    build_executors = [
                        executor.submit(instance.build)
                        for instance in sections_in_progress
                    ]
                    logger.info(f"Sections built in parallel: {len(build_executors)} .")
                self._calculate_expenses(day, sections_in_progress)
            else:
                logger.info('"The Wall" COMPLETED SUCCESSFULLY!')
                logger.info('We are ready for "The Long Winter"!')
                break

    def _create_profile_entries(self) -> None:
        """
        Create profile entries in the database based on the construction parameters.

        This method generates Profile instances for each set of construction parameters
        and saves them to the database.
        """
        for profile_number in range(1, len(self.construction_parameters) + 1):
            profile = Profile(name=profile_number)
            profile.save()
            logger.info(f"Profile {profile_number} stored in the database.")

    def _calculate_expenses(self, day: int, sections: list[Section]) -> None:
        """
        Calculate and log the expenses for each profile based on the sections in progress.

        This method computes the total ice amount needed for construction and
        the associated costs for each profile based on the sections being built.

        Args:
            day (int): The current day of construction (used as a day number for logger).
            sections (list[Section]): The list of sections currently in progress, with crews allocated.

        Raises:
            Profile.DoesNotExist: If the profile queried does not exist in the database.
        """
        for profile_number in range(1, len(self.construction_parameters) + 1):
            ice_amount = sum(
                [
                    section.height_on_day * self.cubics_ice_per_section
                    for section in sections
                    if section.profile_id == profile_number
                ]
            )
            cost = ice_amount * self.price_per_cubic_ice
            logger.info("Calculated costs:")
            logger.info(
                f"Day {day} for profile {profile_number}: ice {ice_amount}, cost {cost}."
            )
            self._write_day_entry(profile_number, day, cost, ice_amount)

    @staticmethod
    def _write_day_entry(profile_id: int, day: int, cost: int, ice: int) -> None:
        """
        Write a day entry to the database for a specific profile.

        Args:
            profile_id (int): The identifier of the profile for which the entry is being created.
            day (int): The day number for the entry.
            cost (int): The cost associated with the amount of ice used on that day.
            ice (int): The amount of ice incurred on that day.

        Raises:
            Profile.DoesNotExist: If the profile with the given ID does not exist.
        """
        day_entry = Day(
            profile=Profile.objects.get(name=profile_id),
            day_number=day,
            cost=cost,
            ice_amount=ice,
        )
        day_entry.save()
        logger.info(f"Day {day} stored in the database.")
        logger.info(f"{day_entry.__dict__}")
