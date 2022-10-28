import paramiko
from django.core.management.base import BaseCommand

from daemon.models import IMacModel


class Command(BaseCommand):
    help = 'Ping the server to see if it is up.'

    def handle(self, *args, **options):
        imacs = IMacModel.objects.all()

        for imac in imacs:
            ssh_client = paramiko.SSHClient()
            ssh_client.connect(hostname=imac.ip, username='LabMac', password='root')
            print(imac.label, imac.ip)
