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
		self

	def OnButtonClick(self):
		subprocess.call(['xterm', '-e',"\"sudo python2 guifrontend.py\""])	
		
	
if __name__ == "__main__":	
	app = mainGUI(None)
	app.title("Triage Program")
	app.mainloop()
	
