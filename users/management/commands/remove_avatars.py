from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    help = f"This commend remove avatars"

    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            user.avatar.delete(save=True)
