from django.core.management.base import BaseCommand
from rooms.models import Facility

NAME = "facilities"


class Command(BaseCommand):

    help = f"This commend creates {NAME}"

    # def Fdd_argfacilitiesmnets(self, parser):
    #     parser.add_argument(
    #         "--number", help="How many facilities do you want to create")
    #     )

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} {NAME} created"))
