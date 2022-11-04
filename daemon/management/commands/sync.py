from django.core.management.base import BaseCommand

from daemon.models import IMacModel
from daemon.utils.sync import sync_mac
from daemon.utils.thread import run_mac_action_async


class Command(BaseCommand):
    help = "Syncs the iMacs state"

    def handle(self, *args, **options):
        print("Syncing iMacs state...")

        imacs = IMacModel.objects.all()
        run_mac_action_async(imacs, sync_mac)
