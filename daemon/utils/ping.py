import paramiko
from django.utils import timezone
from rich import print

from daemon.models import IMacModel
from daemon.utils.ssh import SshClient


def ping_mac(imac: IMacModel):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client = SshClient(ssh_client, imac.ip, imac.mac_user)

        client.close()

        imac.status = IMacModel.MacStatus.AVAILABLE
        imac.last_seen = timezone.now()

        print(f"[bold green]{imac.label} is alive")
    except:
        imac.status = IMacModel.MacStatus.UNAVAILABLE
        print(f"[bold red]{imac.label} is dead")

    imac.save()
