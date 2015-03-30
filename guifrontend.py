#! /usr/bin/python

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


'''
import Tkinter
import subprocess

class mainGUI(Tkinter.Tk):
	def __init__(self, parent):
		Tkinter.Tk.__init__(self, parent)
		self.parent=parent
		self.initialize()
		
	def initialize(self):
		self.osBitString = Tkinter.StringVar()
		self.welcomeString = Tkinter.StringVar()
		self.seperatorString = Tkinter.StringVar()
		self.enterInfoString = Tkinter.StringVar()
		self.theNumber = Tkinter.StringVar()
		self.theNumber.set(u"")

		self.seperatorString.set("--------------------------")
		self.welcomeString.set("Triage data extractor v0.1")
		self.enterInfoString.set("Please enter the triage number:")
		#Strings for all the different things I'm looking for
		self.osBitString.set("OS type: ")

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


		osbittype = Tkinter.Label(self,textvariable=self.osBitString,anchor="w")
		seperator2 = Tkinter.Label(self,textvariable=self.seperatorString,anchor="w")
		beginbutton = Tkinter.Button(self,text=u"Click to begin",command=self.OnButtonClick)
		
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
		osbittype.grid(column=1,row=4,sticky='EW')

		seperator2.grid(column=1,row=5)

		beginbutton.grid(column=1,row=6)



	def checkTriage(self):
		print "TOFO"
		print self.enterNumber.get()
		#checks current inventory
	def OnButtonClick(self):

		self.checkTriage()

		tempString = subprocess.check_output(['uname', '-m'])
		if 'i686' in tempString:
			tempString = "OS type: 32X/32Lite"
		else:
			tempString = "OS type: x86_64"
		self.osBitString.set(tempString)



if __name__ == "__main__":
	app = mainGUI(None)
	app.title("Triage Program")
	app.mainloop()