import os
from logging import Logger
from typing import ClassVar, List
from dataclasses import dataclass, field
from .utilities import setup_logger, logger


LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")


@dataclass
class Crew:
    """Class representing a crew/team of construction workers.

    This class encapsulates the attributes and behaviors of a crew/team
    involved in construction tasks. A crew has an identifier, a height
    that indicates the sections they are initially assigned to work on,
    and a busy status representing their availability for work.

    Attributes:
        number (int): An identifier for the crew.
        section_height (int): The height of the section the crew can work on.
        busy (bool): Indicates whether the crew is currently busy working on a section.
    """

    number: int
    section_height: int
    busy: bool = field(init=False)

    def __post_init__(self) -> None:
        """Post-initialization processing for Crew.

        This method sets the initial busy status of the crew based on
        the height of the sections they are assigned to. If the crew's
        section height is greater than or equal to 30, it marks them
        as available (not busy). Otherwise, they are busy by default.

        """
        self.busy = True
        if self.section_height >= 30:
            logger.info(f"Crew {self.number} has been assigned on a complete section.")
            self.busy = False

    def __str__(self):
        return str(self.number)


@dataclass
class Section:
    """Class representing a single section of The Wall.

    This class handles the construction logic for a section, including managing
    crews, tracking height, and determining completion status.

    Attributes:
        required_height (ClassVar[int]): The required height for the section to be considered complete.
        crews (list[Crew]): A list of Crew instances currently assigned to this section.
        all_crews (list[Crew]): A list of all crews that can be allocated.
        height (int): The current height of the section.
        profile_id (int): The identifier for the profile associated with this section.
        complete (bool): Indicates whether the section is complete (inferred from initialization).
        numb (int): The height of the section at initialization.
        height_on_day (int): Height built on each iteration.
        logger (Logger): logger instance to log in a separate file.
    """

    required_height: ClassVar[int] = 30
    identifier: str
    crews: List[Crew]
    all_crews: List[Crew]
    height: int
    profile_id: int
    height_on_day: int = None
    complete: bool = field(init=False)
    logger: Logger = field(init=False)

    def _prepare_for_build(self) -> None:
        """Prepare the section for building.

        This private method checks if the current height combined with the number of crews
        exceeds the required height if so - releases the appropriate number of crews.
        """
        self.progress = self.height + len(self.crews)
        if self.progress > self.required_height:
            self.logger.info(
                f"Section {self} will gain more height than needed. Releasing crews."
            )
            self._release_crew(self.progress - self.required_height)

    def build(self) -> None:
        """Build the section by adding the height based on the number of crews.

        This method increments the height of the section based on the number of crews assigned.
        It also checks if the section has reached the required height and marks it complete
        if it has.
        """
        self._prepare_for_build()
        self.logger.info(f"Height at beginning of the day - {self.height}")
        self.height += len(self.crews)
        self.logger.info(f"Height build - {len(self.crews)}")
        self.height_on_day = len(self.crews)
        if self.height == self.required_height:
            self.complete = True
            self.logger.info(f"Section {self} has been complete.")
            self._release_crew(len(self.crews))

    def _release_crew(self, quantity: int) -> None:
        """Release a specified number of crews back to the all_crews list.

        This private method updates the busy status of the crews being released and appends
        them back to the all_crews list.

        Args:
            quantity (int): The number of crews to be released.
        """
        for _ in range(quantity):
            crew = self.crews.pop()
            crew.busy = False
            self.all_crews.append(crew)
            self.logger.info(
                f"Crew {crew.number} has been released from section {self}."
            )

    def __post_init__(self) -> None:
        """Post-initialization processing.

        This method sets the initial complete status and may release crews if the initial height
        of the section meets or exceeds the required height.
        """
        self.complete = False
        self.initial_height = self.height
        self.logger = setup_logger(
            name=self.identifier, log_file=f"{LOG_DIR}/{self.identifier}.log"
        )
        if self.initial_height >= self.required_height:
            self.logger.info(f"Section {self} is already complete.")
            self._release_crew(len(self.crews))
            self.complete = True
