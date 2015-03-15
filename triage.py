#! /usr/bin/python
import subprocess
import sys
import os

#Check if the triage sheet was entered as a command line argument
if len(sys.argv) > 1:
	filename = sys.argv[1]
else:	
	filename = raw_input("Please enter CRT number: ")

#Just in case the user enters it as 'L12345.triage'
if not ".triage" in filename:
	filename = filename+ ".triage"

#Create the triage file
txtfile = open(filename + ".triage", "w")

#Check that dmidecode is installed
try:
	subprocess.check_output(['dmidecode', '--version'])
except:
	print "dmidecode is not currently installed on this computer"
	print "this script requires it. Tell Kevin, program exiting"
	exit

print "--------------------------"
txtfile.write("--------------------------\n")

#parsing output of dmidecode for manufacturer, model, and Serial number
manu = subprocess.check_output(['sudo', 'dmidecode', '-t', 'system'])
data = manu.splitlines()
for line in data:
	if "Manufacturer" in line:
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
#variables for hardware devices
USB = False
ETHERNET = False
VGA = False
DVI = False
HDMI = False
#PS2 is not currently checked for
#for some strange reason I can't find
#a way to list ports from the terminal
PS2 = False
WIFI = False

#parsing lspci for hardware devices
data = subprocess.check_output(['lspci'])
data = data.splitlines()
for line in data:
	if "USB controller" in line:
		USB = True
	if "Ethernet controller" in line:
		ETHERNET = True
	if "Network controller" in line:
		WIFI = True
	if "VGA compatible" in line:
		VGA = True
	#NEEDS TESTED
	if "DVI" in line:
		DVI = True
	#NEEDS TESTED
	if "HDMI" in line:
		HDMI = True
		
print "--------------------------"
txtfile.write("--------------------------\n")

print "Video Devices:"
txtfile.write("Video Devices:")
if VGA:
	print "-VGA"
	txtfile.write(" VGA\n")
if DVI:
	print "-DVI"
	txtfile.write(" DVI\n")
if HDMI:
	print "-HDMI"
	txtfile.write(" HDMI\n")
	
print "--------------------------"
txtfile.write("--------------------------\n")

print "Ports:"
txtfile.write("Ports:\n")
if ETHERNET:
	print "-ETHERNET"
	txtfile.write(" ETHERNET\n")
if USB:
	print "-USB"
	txtfile.write(" USB\n")
if PS2:
	print "-PS/2"
	txtfile.write(" PS/2\n")
print "--------------------------"
txtfile.write("--------------------------\n")

hddsize = subprocess.check_output(['sudo', 'fdisk', '-l'])
hddsize = hddsize.splitlines()
for line in hddsize:
	if "Disk /dev/sda" in line:
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

print "--------------------------"
txtfile.write("--------------------------\n")

#This code is Ubuntu specific, if using another os it will 
#throw an error
osversion = subprocess.check_output(['more', '/etc/lsb-release'])
osversion = osversion.splitlines()
for line in osversion:
	if "RELEASE" in line:
		os = line
print "Final Ubuntu OS: " + os.replace("DISTRIB_RELEASE=","")
txtfile.write("Final Ubuntu OS: " + os.replace("DISTRIB_RELEASE=","")+ "\n")

print "--------------------------"
txtfile.write("--------------------------\n")

#parse dmidecode for processor information
processor = subprocess.check_output(['sudo', 'dmidecode', '-t', 'processor'])
processor = processor.splitlines()
for line in processor:
	if "Max Speed" in line:
		line = line.replace('\t','')
		print "Processor speed: " + line.replace("Max Speed: ","")
		txtfile.write("Processor speed: " + line.replace("Max Speed: ","")+"\n")

print "--------------------------"
txtfile.write("--------------------------\n")

#Get and parse the RAM size from /proc/meminfo
#it is originally given in kB, so convert to MB
#by dividing by 1000
raminfo = subprocess.check_output(['cat', '/proc/meminfo'])
raminfo = raminfo.splitlines()
raminfo = raminfo[0].replace(" ","")
raminfo = raminfo.replace("kB","")
raminfo = raminfo.replace("MemTotal:","")
print "Memory: " + str(int(raminfo)/1000) + " MB"
txtfile.write("Memory: " + str(int(raminfo)/1000) + " MB\n")

print "--------------------------"
txtfile.write("--------------------------\n")

#check if computer is wifi enabled
#if the laptop is missing drivers this may
#give a false bas reading
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
#os.system("scp " + filename + "10.0.88.)
