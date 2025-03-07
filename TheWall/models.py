from django.db import models


class Profile(models.Model):
    """
    Represents a profile for a user or entity.

    Attributes:
        name (int): An integer representing the profile identifier or some significant numeric attribute.

    Methods:
        __str__() -> str: Returns a string representation of the profile name.
    """

    name = models.IntegerField()

    def __str__(self):
        """
        Returns a string representation of the Profile instance.

        Returns:
            str: The string representation of the profile's name as an integer.
        """
        return str(self.name)


class Day(models.Model):
    """
    Represents a day for a specific profile with associated costs and ice amounts.

    Attributes:
        profile (ForeignKey): The profile associated with this day, linked to the Profile model.
        day_number (int): The day number associated with this entry.
        cost (int): The cost for the associated day.
        ice_amount (int): The amount of ice related to the day's activities.

    Meta:
        unique_together: Ensures that each profile can only have one entry for each day number.

    Methods:
        __str__() -> str: Returns a string representation of the Day instance.
    """

    profile = models.ForeignKey(Profile, related_name="days", on_delete=models.CASCADE)
    day_number = models.IntegerField()
    cost = models.IntegerField()
    ice_amount = models.IntegerField()

    class Meta:
        """Set's up a pair of keys as a primary key. a.k.a. profile and day_number"""

        unique_together = ("profile", "day_number")

    def __str__(self):
        """
        Returns a string representation of the Day instance.

        Returns:
            str: A string indicating the day number and the associated profile's name.
        """
        return f"Day {self.day_number} for {self.profile.name}"
