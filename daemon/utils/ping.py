import paramiko
from django.utils import timezone
from rich import print

from daemon.models import IMacModel
from daemon.utils.notification import send_imac_status_notification
from daemon.utils.ssh import SshClient


def ping_mac(imac: IMacModel):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    current_status = imac.status

    try:
        client = SshClient(ssh_client, imac.ip, imac.mac_user)

        imac.status = IMacModel.MacStatus.AVAILABLE
        imac.last_seen = timezone.now()

        stdout = client.run_command_and_get_stdout("who | grep console")
        if stdout:
            imac.status = IMacModel.MacStatus.IN_USE

        client.close()

        print(f"[bold green]{imac.label} is alive")
    except:
        imac.status = IMacModel.MacStatus.UNAVAILABLE
        print(f"[bold red]{imac.label} is dead")

    imac.save()

    if current_status != imac.status and imac.report_status:
        send_imac_status_notification(imac)
