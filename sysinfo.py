import sys
import os
import platform
import subprocess

print(sys.platform)
print(sys.version)
print(sys.getfilesystemencoding())
print(sys.getdefaultencoding())
print(sys.path)

pwd = os.getcwd()
list_directory = os.listdir(pwd)
for directory in list_directory:
    print(directory)


operating_system = platform.system()
print(operating_system)

subprocess.run('dir', shell=True)

for file in os.walk(pwd):
    print(file)