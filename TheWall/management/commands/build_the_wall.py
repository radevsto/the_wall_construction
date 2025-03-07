from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import transaction
from TheWall.construction_manager import ConstructionManager as BranTheBuilder


class Command(BaseCommand):
    """
    Command to execute the business logic of the app.
    Each run(simulation) is separate, thus the database is flushed.
    """

    help = "Simulates building The Wall!"

    def handle(self, *args, **options):
        self.stdout.write("Flushing the database...")
        with transaction.atomic():
            call_command("flush", interactive=False, reset_sequences=True)
        self.stdout.write("Database flush complete.")

        Bran = BranTheBuilder()
        Bran.build_the_wall()
