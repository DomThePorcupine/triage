#!/usr/bin/python
import Tkinter
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
		print "Yay"
		self.labelVariable.set("You clicked the button !")
		
if __name__ == "__main__":
	app = mainGUI(None)
	app.title("Triage Program")
	app.mainloop()
	
	
