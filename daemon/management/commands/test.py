from django.core.management.base import BaseCommand

from daemon.models import IMacModel
from daemon.utils.notification import  send_imac_status_notification
from daemon.utils.ping import ping_mac
from daemon.utils.thread import run_mac_action_async


class Command(BaseCommand):
    help = 'Test command.'

    def handle(self, *args, **options):
        print('Testings...')

        send_imac_status_notification(None)