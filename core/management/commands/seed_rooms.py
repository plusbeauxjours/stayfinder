import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models

NAME = "rooms"


class Command(BaseCommand):

    help = f"This commend creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many {NAME} you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        all_room_types = room_models.RoomType.objects.all()
        all_amenities = room_models.Amenity.objects.all()
        all_facilities = room_models.Facility.objects.all()
        all_rules = room_models.HouseRule.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(all_room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 17)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1,17)}.webp",
                )
        for a in all_amenities:
            magic_number = random.randint(0, 15)
            if magic_number % 2 == 0:
                room.amenities.add(a)
        for f in all_facilities:
            magic_number = random.randint(0, 15)
            if magic_number % 2 == 0:
                room.facilities.add(f)
        for r in all_rules:
            magic_number = random.randint(0, 15)
            if magic_number % 2 == 0:
                room.rules.add(r)
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created"))
