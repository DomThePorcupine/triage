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
		button = Tkinter.Button(self,text="Click to begin!",command=self.OnButtonClick)
		button.grid(column=0,row=0)
	def OnButtonClick(self):
		self.destroy()
		
			
		
		
	
if __name__ == "__main__":	
	app = mainGUI(None)
	app.title("Triage Laucncher")
	app.mainloop()
	os.system("xterm -e \"sudo python2 guifrontend.py & sleep 5 & exit\"")
