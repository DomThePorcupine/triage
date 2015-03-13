#! /usr/bin/python
import subprocess
import sys
import os
filename = raw_input("Please enter CRT number: ")
txtfile = open(filename + ".triage", "w")
filename = filename+ ".triage"
print "--------------------------"
txtfile.write("--------------------------\n")
manu = subprocess.check_output(['sudo', 'dmidecode', '-t', 'system'])
data = manu.splitlines()
for line in data:
	if "Manu" in line:
		print line.replace('\t','')
		txtfile.write(line.replace('\t','')+"\n")
		print "--------------------------"
		txtfile.write("--------------------------\n")
	if "Version" in line:
		line = line.replace('\t','')
		print line.replace("Version", "Model")
		txtfile.write(line.replace("Version", "Model")+ "\n")
		print "--------------------------"
		txtfile.write("--------------------------\n")
	if "Serial" in line:
		print line.replace('\t','')
		txtfile.write(line.replace('\t','') + "\n")

data = subprocess.check_output(['lspci'])
data = data.splitlines()
USB = False
ETHERNET = False
VGA = False
DVI = False
HDMI = False
PS2 = False
WIFI = True
for line in data:
	if "USB controller" in line:
		USB = True
	if "Ethernet controller" in line:
		ETHERNET = True
	if "Network controller" in line:
		WIFI = True
	if "VGA compatible" in line:
		VGA = True
	if "DVI" in line:
		DVI = True 
	if "HDMI" in line:
		HDMI = True
print "--------------------------"
txtfile.write("--------------------------\n")
print"Video Devices:"
txtfile.write("Video Devices:")
if VGA:
	print " VGA"
	txtfile.write(" VGA\n")
if DVI:
	print " DVI"
	txtfile.write(" DVI\n")
if HDMI:
	print " HDMI"
	txtfile.write(" HDMI\n")
print "--------------------------"
txtfile.write("--------------------------\n")
print"Ports:"
txtfile.write("Ports:\n")
if ETHERNET:
	print " ETHERNET"
	txtfile.write(" ETHERNET\n")
if USB:
	print " USB"
	txtfile.write(" USB\n")
if PS2:
	print " PS/2"
	txtfile.write(" PS/2\n")
print "--------------------------"
txtfile.write("--------------------------\n")

p = subprocess.check_output(['sudo', 'fdisk', '-l'])
data = p.splitlines()
for line in data:
	if "Disk /dev" in line:
		data2 = line
data2 = data2.split(" ")
print "Hard Drive: " + data2[2] + "GB"
txtfile.write("Hard Drive: " + data2[2] + "GB\n")

cdrom = subprocess.check_output(['cat', '/proc/sys/dev/cdrom/info'])
cdrom = cdrom.splitlines()
CD=False
DVD=False
CDR=False
DVDR=False
for line in cdrom:
	if "play audio" in line and '1' in line:
		CD=True
	if "read DVD" in line and '1' in line:
		DVD=True
	if "write DVD-R" in line and '1' in line:
		DVDR=True
	if "write CD-RW" in line and '1' in line:
		CDR=True
print "--------------------------"
txtfile.write("--------------------------\n")
if CD and not DVD:
	print "CD/DVD Drive: CD"
	txtfile.write("CD/DVD Drive: CD\n")
if CD and DVD and not CDR and not DVDR:
	print "CD/DVD Drive: CD-DVD"
	txtfile.write("CD/DVD Drive: CD-DVD\n")
if CDR and DVD and not DVDR:
	print "CD/DVD Drive: CD-RW/DVD"
	txtfile.write("CD/DVD Drive: CD-RW/DVD\n")
if CDR and DVDR:
	print "CD/DVD Drive: CD_RW/DVD-RW"
	txtfile.write("CD/DVD Drive: CD_RW/DVD-RW\n")
osversion = subprocess.check_output(['more', '/etc/lsb-release'])
osversion = osversion.splitlines()
for line in osversion:
	if "RELEASE" in line:
		os = line
print "--------------------------"
txtfile.write("--------------------------\n")
print "Final Ubuntu OS: " + os.replace("DISTRIB_RELEASE=","")
txtfile.write("Final Ubuntu OS: " + os.replace("DISTRIB_RELEASE=","")+ "\n")

processor = subprocess.check_output(['sudo', 'dmidecode', '-t', 'processor'])
processor = processor.splitlines()
print "--------------------------"
txtfile.write("--------------------------\n")
for line in processor:
	if "Max Speed" in line:
		line = line.replace('\t','')
		print "Processor speed: " + line.replace("Max Speed: ","")
		txtfile.write("Processor speed: " + line.replace("Max Speed: ","")+"\n")

raminfo = subprocess.check_output(['cat', '/proc/meminfo'])
raminfo = raminfo.splitlines()
raminfo = raminfo[0].replace(" ","")
raminfo = raminfo.replace("kB","")
raminfo = raminfo.replace("MemTotal:","")
print "--------------------------"
txtfile.write("--------------------------\n")
print "Memory: " + str(int(raminfo)/1000) + " MB"
txtfile.write("Memory: " + str(int(raminfo)/1000) + " MB\n")
print "--------------------------"
txtfile.write("--------------------------\n")
if WIFI:
	print "Wifi enabled"
	txtfile.write("Wifi available\n")
else:
	print "No wifi"
	txtfile.write("No wifi\n")
print "--------------------------"
txtfile.write("--------------------------\n")
txtfile.close()
#The following command basically gives you a bash shell
#anything in " " will get executed as if you typed it into the terminal
#example os.system("echo \"you are my only sunshine\" >> afile.txt")
#filename = file.triage that is created
os.system("scp " + filename + "10.0.88.)
