import threading

import paramiko
from django.utils import timezone
from rich import print

from daemon.models import IMacModel


def ping(imac: IMacModel):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(imac.ip, username=imac.mac_user, timeout=10)
        ssh_client.close()

        imac.alive = True
        imac.last_seen = timezone.now()

        print(f"[bold green]{imac.label} is alive")
    except:
        imac.alive = False
        print(f"[bold red]{imac.label} is dead")

    imac.save()


def async_ping():
    imacs = IMacModel.objects.all()

    threads = []

    for imac in imacs:
        th = threading.Thread(target=ping, args=(imac,))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()
