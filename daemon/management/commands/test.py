from django.core.management.base import BaseCommand

from daemon.models import IMacModel
from daemon.utils.notification import send_imac_status_notification


class Command(BaseCommand):
    help = 'Test command.'

    def handle(self, *args, **options):
        print('Testings...')

        imac = IMacModel.objects.all()[0]
        imac.status = IMacModel.MacStatus.IN_USE
        send_imac_status_notification(imac)
