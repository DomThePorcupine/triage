#! /usr/bin/python2
#simple launcher so that
#our main program is run as sudo

import Tkinter
import subprocess
import os
class mainGUI(Tkinter.Tk):
	def __init__(self, parent):
		Tkinter.Tk.__init__(self, parent)
		self.parent=parent
		self.initialize()
		
	def initialize(self):
		button = Tkinter.Button(self,text="Click here to launch GUI (Recommended)",command=self.OnButtonClick)
		buttonCLI = Tkinter.Button(self,text="Click here for CLI (Admin/Kevin/Dom)",command=self.OnCLIButtonClick)
		button.grid(column=0,row=0)
		buttonCLI.grid(column=0,row=1)
	def OnButtonClick(self):
		
		os.system("xterm -e \"sudo python2 /usr/local/bin/guifrontend.py\"")
		self.destroy()
	def OnCLIButtonClick(self):
		os.system("xterm -e \"sudo python2 /usr/local/bin/triage.py\"")
		self.destroy()
class updater(Tkinter.Tk):
	def __init__(self, parent):
		Tkinter.Tk.__init__(self, parent)
		self.parent=parent
		self.initialize()
	def initialize(self):
		words = Tkinter.Label(self,text="Please update to continue:",anchor="w")
		button = Tkinter.Button(self,text="UPDATE",command=self.OnButtonClick)
		button.grid(column=0,row=1)
		words.grid(column=0,row=0)
	def OnButtonClick(self):
		os.system("xterm -e \"sudo apt-get install wget; sudo wget https://raw.githubusercontent.com/DomThePorcupine/triage/master/triage.py -O /usr/local/bin/triage.py; sudo wget https://raw.githubusercontent.com/DomThePorcupine/triage/master/guifrontend.py -O /usr/local/bin/guifrontend.py; read x\"")
		self.destroy()
		
		
		

if __name__ == "__main__":
	update = updater(None)
	update.title("Triage updater")
	update.mainloop()
	
	app = mainGUI(None)
	app.title("Triage Laucncher")
	app.mainloop()

