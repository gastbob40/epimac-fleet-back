from paramiko.client import SSHClient


class SshClient:
    def __init__(self, ssh_client: SSHClient, ip: str, username: str):
        self.ssh_client = ssh_client
        ssh_client.connect(ip, username=username)

    def run_command_and_get_stdout(self, command: str) -> str:
        _, stdout, _ = self.ssh_client.exec_command(command)
        stdout.channel.recv_exit_status()
        return stdout.read().decode("utf-8").strip()

    def close(self):
        self.ssh_client.close()
