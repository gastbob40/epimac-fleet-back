import paramiko
from django.core.management.base import BaseCommand

from daemon.models import IMacModel
from daemon.utils.ssh import SshClient


class Command(BaseCommand):
    help = "Syncs the iMacs state"

    def handle(self, *args, **options):
        print("Syncing iMacs state...")

        imacs = IMacModel.objects.all()

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        for imac in imacs:
            client = SshClient(ssh_client, imac.ip, imac.mac_user)

            imac.macos_version = client.run_command_and_get_stdout("sw_vers -productVersion")
            imac.macos_build_version = client.run_command_and_get_stdout("sw_vers -buildVersion")
            imac.serial_number = client.run_command_and_get_stdout("system_profiler SPHardwareDataType | grep 'Serial Number' | awk '{print $4}'")

            storage_str = client.run_command_and_get_stdout("system_profiler SPStorageDataType | grep 'Capacity'")
            imac.storage_capacity = float(storage_str.split(":")[1].strip().split(" ")[0].replace(",", "."))

            memory_str = client.run_command_and_get_stdout("system_profiler SPHardwareDataType | grep 'Memory'")
            imac.memory = int(memory_str.split(":")[1].strip().split(" ")[0])

            cores_str = client.run_command_and_get_stdout("system_profiler SPHardwareDataType | grep 'Total Number of Cores'")
            imac.cpu_cores = int(cores_str.split(":")[1].strip().split(" ")[0])

            client.close()

            imac.save()
