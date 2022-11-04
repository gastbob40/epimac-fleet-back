from django.core.management.base import BaseCommand

from daemon.models import IMacModel
from daemon.utils.ping import ping_mac
from daemon.utils.thread import run_mac_action_async


class Command(BaseCommand):
    help = 'Ping the server to see if it is up.'

    def handle(self, *args, **options):
        print('Pinging iMacs...')

        imacs = IMacModel.objects.all()
        run_mac_action_async(imacs, ping_mac)
