from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        User.objects.create_superuser(
            username='admin',
            password='admin123',
            email='admin@gmail.com'
        )
        self.stdout.write(self.style.SUCCESS('Successfully created an admin!'))
