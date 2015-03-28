#!/usr/bin/python
import Tkinter
import subprocess
class mainGUI(Tkinter.Tk):
	def __init__(self, parent):
		Tkinter.Tk.__init__(self, parent)
		self.parent=parent
		self.initialize()
		
	def initialize(self):
		self.grid()
		#button
		button = Tkinter.Button(self,text=u"Click to begin",command=self.OnButtonClick)
		button.grid(column=1,row=0)
		#fg=foregorund bg = background
		
		#usefull for outputing the info to the user
		self.labelVariable = Tkinter.StringVar()
		
		
		label = Tkinter.Label(self,textvariable=self.labelVariable,anchor="w",fg="white",bg="blue")
		label.grid(column=1,row=1,sticky='EW')
		
	def OnButtonClick(self):
		osbittype = subprocess.check_output(['uname', '-m'])
		if 'i686' in osbittype:
			osbittype = "OS type: 32X/32Lite"
		else:
			osbittype = "OS type: x86_64"
		self.labelVariable.set(osbittype)
		
if __name__ == "__main__":
	app = mainGUI(None)
	app.title("Triage Program")
	app.mainloop()
	
	
