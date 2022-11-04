from django.core.management.base import BaseCommand

from daemon.utils.sync import async_sync


class Command(BaseCommand):
    help = "Syncs the iMacs state"

    def handle(self, *args, **options):
        print("Syncing iMacs state...")

        async_sync()
