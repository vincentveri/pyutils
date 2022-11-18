from sys import stdin
from paramiko import SSHClient
import paramiko
import config as cfg

client = SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(cfg.ssh["host"], username=cfg.ssh["user"], password=cfg.ssh["password"])
stdin, stdout, stderr = client.exec_command('ls -lha | grep wget')
output = stdout.read()
client.close()

print(output.decode())
