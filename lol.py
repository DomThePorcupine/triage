#! /usr/bin/python
import subprocess
print subprocess.check_output(['sudo', 'dmidecode'])
