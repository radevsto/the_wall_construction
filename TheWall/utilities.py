import logging
from .custom_exceptions import ExceededNumberOfSections, ExceededHighOfSections


class ConfigReader:
    """
    A class to read and validate construction parameters from a file.

    Attributes:
        max_number_of_sections (int): The maximum number of sections allowed.
        required_section_high (int): The maximum height allowed for a section.

    Args:
        construction_doc (str): The path to the input file containing construction parameters.
    """

    max_number_of_sections = 2000
    required_section_high = 30

    def __init__(self, construction_doc: str) -> None:
        """
        Initialize the ConfigReader with the path to the input file.

        Args:
            construction_doc (str): The path to the input file containing construction parameters.
        """
        self.input_file = construction_doc

    def _get_input(self) -> list[list[int]]:
        """
        Read the input file and convert it to a list of lists of integers.

        Returns:
            list[list[int]]: A list of profiles, each profile being a list of integers.

        Raises:
            FileNotFoundError: If the specified input file cannot be found.
        """
        try:
            with open(self.input_file, "r") as input_file:
                return [
                    list(map(int, profile.split()))
                    for profile in input_file.read().splitlines()
                ]
        except FileNotFoundError:
            raise FileNotFoundError(f"Input file missing: {self.input_file}")

    def _validate_input(self) -> list[list[int]]:
        """
        Validate the input data read from the input file.

        Each profile in the input is checked to ensure it does not exceed the maximum
        number of sections and does not contain heights greater than the required height.

        Returns:
            list[list[int]]: The validated input data.

        Raises:
            ExceededNumberOfSections: If any profile has more sections than allowed.
            ExceededHighOfSections: If any section height exceeds the required height.
        """
        input_data = self._get_input()
        for num, profile in enumerate(input_data):
            if len(profile) > self.max_number_of_sections:
                raise ExceededNumberOfSections(
                    len(profile), self.max_number_of_sections, num
                )
            if any(sec > self.required_section_high for sec in profile):
                raise ExceededHighOfSections(self.required_section_high, num)

        return input_data

    def get_data(self) -> list[list[int]]:
        """
        Retrieve and validate the construction parameters.

        This method combines both reading the input from the file and validating it.

        Returns:
            list[list[int]]: The validated construction parameters.

        Raises:
            ExceededNumberOfSections: If any profile exceeds the maximum number of sections.
            ExceededHighOfSections: If any section height exceeds the required height.
        """
        return self._validate_input()


logger = logging.getLogger("TheWall")
