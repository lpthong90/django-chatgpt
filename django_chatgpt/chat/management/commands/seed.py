from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Initialize seed data"

    def handle(self, *args, **options):
        user_1 = User.objects.create_user('user_1', 'user_1@email.com', 'password')
        user_1.save()
        user_2 = User.objects.create_user('user_2', 'user_2@email.com', 'password')
        user_2.save()
        user_3 = User.objects.create_user('user_3', 'user_3@email.com', 'password')
        user_3.save()

