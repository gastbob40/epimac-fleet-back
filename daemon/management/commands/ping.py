from django.core.management.base import BaseCommand

from daemon.utils.ping import async_ping


class Command(BaseCommand):
    help = 'Ping the server to see if it is up.'

    def handle(self, *args, **options):
        async_ping()
