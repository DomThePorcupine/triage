#! /usr/bin/python2

'''
How I want the program to look:
   c1         c2           c3
/-----/-----------------/-----/

|-----------------------------| R1
|-----Welcome screen v0.1-----| R2
|-----------------------------| R3
|-----Select one of these-----| R4
|-----Mac(*) or Linux(*) -----| R5
|-----------------------------| R6
|-----Enter triage number-----| R7
|-----|~~~~TEXT  BOX~~~~|-----| R8
|-----------------------------| R9
|-----|Click to begin tr|-----| R11
|-----------------------------| R12

Manufact
Serial #
Models #
Ram info
HDD info
Wifi y/n
osbit ty
ubuntu v
CD-R/DVD
video ps
-VGA
-DVI
HDMI
ot ports
ethnet
USB
PS/2

'''
import Tkinter
import subprocess
import os
class mainGUI(Tkinter.Tk):
	def __init__(self, parent):
		Tkinter.Tk.__init__(self, parent)
		self.parent=parent
		
		self.initialize()
		
	def initialize(self):
		
		self.welcomeString = Tkinter.StringVar()
		self.seperatorString = Tkinter.StringVar()
		self.enterInfoString = Tkinter.StringVar()
		self.theNumber = Tkinter.StringVar()
		self.checkABox = Tkinter.StringVar()
		
		#Defining label strings
		self.manufacturer = Tkinter.StringVar()
		self.model = Tkinter.StringVar()
		self.serial = Tkinter.StringVar()
		self.video = Tkinter.StringVar()
		self.port = Tkinter.StringVar()
		self.hdd = Tkinter.StringVar()
		self.cddvd = Tkinter.StringVar()
		self.ubuntu = Tkinter.StringVar()
		self.processor = Tkinter.StringVar()
		self.ram = Tkinter.StringVar()
		self.wifi = Tkinter.StringVar()
		self.osbit = Tkinter.StringVar()
		
		#Add string info
		self.manufacturer.set("Manufacturer: ")
		self.model.set("Model: ")
		self.serial.set("Serial Number: ")
		self.video.set("Video Devices: ")
		self.port.set("Ports: ")
		self.hdd.set("Hard Drive: ")
		self.cddvd.set("CD/DVD Drive: ")
		self.ubuntu.set("Final Ubuntu OS: ")
		self.processor.set("Processor speed: ")
		self.ram.set("Memory: ")
		self.wifi.set("Wifi enabled: ")
		self.osbit.set("OS type: ")
		
		self.linux = Tkinter.IntVar()
		self.linux.set(0)
		
		self.mac = Tkinter.IntVar()
		self.mac.set(0)
		
		self.seperatorString.set("--------------------------")
		self.welcomeString.set("Triage data extractor v0.1")
		self.enterInfoString.set("Please enter the triage number:")
		self.theNumber.set(u"")
		self.checkABox.set("Please select ONE of the following:")
		
		photo = Tkinter.PhotoImage(file = "cr.gif")
		
		self.grid()

		logoHeader1 = Tkinter.Label(self,image=photo)
		logoHeader1.image = photo
		logoHeader2 = Tkinter.Label(self,image=photo)
		logoHeader2.image = photo

		welcomeLabel = Tkinter.Label(self,textvariable=self.welcomeString,anchor="w")
		seperator1 = Tkinter.Label(self,textvariable=self.seperatorString,anchor="w")
		enterInfoLabel = Tkinter.Label(self,textvariable=self.enterInfoString,anchor="w")
		enterNumber = Tkinter.Entry(self, textvariable=self.theNumber)
		checkBoxLabel = Tkinter.Label(self,text="Please select ONE of the following:",anchor="w")
		linuxCheckBox = Tkinter.Checkbutton(self,text="Linux",variable=self.linux)
		macCheckBox = Tkinter.Checkbutton(self,text="Mac",variable=self.mac)
		seperator2 = Tkinter.Label(self,textvariable=self.seperatorString,anchor="w")
		beginbutton = Tkinter.Button(self,text=u"Click to begin",command=self.OnButtonClick)

		manus = Tkinter.Label(self,textvariable=self.manufacturer,anchor="w")
		models = Tkinter.Label(self,textvariable=self.model,anchor="w")
		serials = Tkinter.Label(self,textvariable=self.serial,anchor="w")
		videos = Tkinter.Label(self,textvariable=self.video,anchor="w")
		ports = Tkinter.Label(self,textvariable=self.port,anchor="w")
		hdds = Tkinter.Label(self,textvariable=self.hdd,anchor="w")
		cddvds = Tkinter.Label(self,textvariable=self.cddvd,anchor="w")
		ubuntus = Tkinter.Label(self,textvariable=self.ubuntu,anchor="w")
		processors = Tkinter.Label(self,textvariable=self.processor,anchor="w")
		rams = Tkinter.Label(self,textvariable=self.ram,anchor="w")
		wifis = Tkinter.Label(self,textvariable=self.wifi,anchor="w")
		osbits = Tkinter.Label(self,textvariable=self.osbit,anchor="w")
		#In order of row for my sanity

		#Row 0
		logoHeader1.grid(column=0,row=0)
		logoHeader2.grid(column=2,row=0)
		welcomeLabel.grid(column=1,row=0)
		#Row 1
		seperator1.grid(column=1,row=1)
		#Row 2
		enterInfoLabel.grid(column=1,row=2)
		enterNumber.grid(column=1,row=3)
		
		#Row 4
		checkBoxLabel.grid(column=1,row=4)
		#Row 5
		linuxCheckBox.grid(column=1,row=5,sticky="w")
		macCheckBox.grid(column=1,row=5)
		seperator2.grid(column=1,row=6)
		
		
		manus.grid(column=1,row=7,sticky='EW')
		models.grid(column=1,row=8,sticky='EW')
		serials.grid(column=1,row=9,sticky='EW')
		videos.grid(column=1,row=10,sticky='EW')
		ports.grid(column=1,row=11,sticky='EW')
		hdds.grid(column=1,row=12,sticky='EW')
		cddvds.grid(column=1,row=13,sticky='EW')
		ubuntus.grid(column=1,row=14,sticky='EW')
		processors.grid(column=1,row=15,sticky='EW')
		rams.grid(column=1,row=16,sticky='EW')
		wifis.grid(column=1,row=17,sticky='EW')
		osbits.grid(column=1,row=18,sticky='EW')
		
		beginbutton.grid(column=1,row=19)
	
	def cpuPopUp(self):
		top = Tkinter.Toplevel()
		top.title("YOU CHOSE POORLY")
		msg = Tkinter.Label(top, text="Choose only one, Linux or Mac")
		msg.pack()
		button = Tkinter.Button(top, text="I understand I was wrong", command=top.destroy)
		button.pack()
		
	def numPopUp(self):
		top = Tkinter.Toplevel()
		top.title("INVALID TRIAGE NUMBER")
		msg = Tkinter.Label(top, text="Please enter a triage number!")
		msg.pack()
		button = Tkinter.Button(top, text="I understand I was wrong", command=top.destroy)
		button.pack()
	

	
	def checkTriage(self):
		#work out commands to check all the files for conflicting names
		#if number exists in directory
			#fileExistsPopUp
		if self.theNumber.get() == "":
			self.numPopUp()
		elif self.linux.get() == self.mac.get():
			self.cpuPopUp()
		if self.theNumber.get() != "" and self.linux.get() != self.mac.get():
			return "L" + theNumber.get()
			
			
	def cdCheck(self):
		CD=False
		DVD=False
		CDR=False
		DVDR=False
		
		try:
			cdrom = subprocess.check_output(['cat', '/proc/sys/dev/cdrom/info'])
		except:
			return "CD/DVD Drive:\tN/A"	
		cdrom = cdrom.splitlines()
		for line in cdrom:
			if "play audio" in line and '1' in line:
				CD=True
			if "read DVD" in line and '1' in line:
				DVD=True
			if "write DVD-R" in line and '1' in line:
				DVDR=True
			if "write CD-RW" in line and '1' in line:
				CDR=True
		if CD and not DVD:
			return "CD/DVD Drive:\t\tCD"
		if CD and DVD and not CDR and not DVDR:
			return "CD/DVD Drive:\t\tCD/DVD"
		if CDR and DVD and not DVDR:
			return "CD/DVD Drive:\tCD-RW/DVD"
		if CDR and DVDR:
			return "CD/DVD Drive:\tCD-RW/DVD-RW"
		return "N/A"
		
	def osBitCheck(self):
		osbitc = subprocess.check_output(['uname', '-m'])
		if 'i686' in osbitc:
			return "OS type:\t\t32X/32Lite"
		else:
			return "OS type:\t\tx86_64"
	def manuCheck(self):
		manu = subprocess.check_output(['sudo','dmidecode','-t','system']);
		data = manu.splitlines()
		for line in data:
			if "Manufacturer" in line:
				line = line.replace('\t','')
				return line.replace(':',':\t')
		
	def serialCheck(self):
		serial = subprocess.check_output(['sudo','dmidecode','-t','system'])
		data = serial.splitlines()
		for line in data:
			if "Serial" in line:
				line = line.replace('\t','')
				return line.replace(':',':\t')
	
	def memCheck(self):
		raminfo = subprocess.check_output(['cat', '/proc/meminfo'])
		raminfo = raminfo.splitlines()
		raminfo = raminfo[0].replace(" ","")
		raminfo = raminfo.replace("kB","")
		raminfo = raminfo.replace("MemTotal:","")
		return "Memory:\t\t" + str(int(raminfo)/1000) + " MB"
		
	def protsCheck(self):
		processor = subprocess.check_output(['sudo', 'dmidecode', '-t', 'processor'])
		processor = processor.splitlines()
		for line in processor:
			if "Max Speed" in line:
				line = line.replace('\t','')
				return "Processor speed:\t" + line.replace("Max Speed: ","")
	def hddCheck(self):
		hddsize = subprocess.check_output(['sudo','fdisk','-l'])
		hddsize = hddsize.splitlines()
		for line in hddsize:
			if "Disk /dev/sda" in line:
				data2 = line
		data2 = data2.split(" ")
		return "Hard Drive:\t" + data2[2] + " GB"
	def portCheck(self):
		PS2=False
		ps = subprocess.check_output(['sudo', 'dmidecode'])
		ps = ps.splitlines()
		for line in ps:
			if "PS/2" in line:
				PS2=True
		returnString = ""
		data = subprocess.check_output(['lspci'])
		data = data.splitlines()
		for line in data:
			if "USB controller" in line:
				returnString = "USB"
			if "Ethernet controller" in line:
				returnString = returnString + "\Ethernet"
			if PS2: 
				returnString = returnString + "\PS/2"

		return "Ports:\t" + returnString
				
	def OnButtonClick(self):
		self.checkTriage()
		self.cddvd.set(self.cdCheck())
		self.osbit.set(self.osBitCheck())
		self.ram.set(self.memCheck())
		self.processor.set(self.protsCheck())
		self.manufacturer.set(self.manuCheck())
		self.serial.set(self.serialCheck())
		self.hdd.set(self.hddCheck())
		self.port.set(self.portCheck())	
if __name__ == "__main__":	
	app = mainGUI(None)
	app.title("Triage Program")
	app.mainloop()
	
	
	
	
	
	
	
	
	
	
