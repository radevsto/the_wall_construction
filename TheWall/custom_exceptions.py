class ExceededNumberOfSections(Exception):
    """
    Exception raised when the number of sections exceeds the allowed limit for a profile.
    """

    def __init__(self, quantity: int, limit: int, profile_num: int):
        """
        Initialize the ExceededNumberOfSections exception with a message.

        Args:
            quantity (int): The number of sections that exceeded the limit.
            limit (int): The maximum allowed number of sections.
            profile_num (int): The profile identifier for contextual error reporting.
        """
        self.message = (
            f"{quantity} of profile {profile_num} is higher than the limit of {limit}!"
        )
        super().__init__(self.message)


class ExceededHeightOfSections(Exception):
    """
    Exception raised when a profile contains sections higher than the allowed limit.
    """

    def __init__(self, limit: int, profile_num: int) -> None:
        """
        Initialize the ExceededHeightOfSections exception with a message.

        Args:
            limit (int): The maximum allowed height for a section.
            profile_num (int): The profile identifier for contextual error reporting.
        """
        self.message = f"Profile {profile_num} contains section/s higher than the limit of: {limit}!"
        super().__init__(self.message)
