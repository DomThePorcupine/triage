#!/usr/bin/python
import Tkinter
class mainGUI(Tkinter.Tk):
	def __init__(self, parent):
		Tkinter.Tk.__init__(self, parent)
		self.parent=parent
		self.initialize()
		
	def initialize(self):
		self.grid()
		#text entry
		self.entry = Tkinter.Entry(self)
		self.entry.grid(column=0,row=0,sticky='EW')
		self.entry.bind("<Return>", self.OnPressEnter)
		#button
		button = Tkinter.Button(self,text=u"Click to begin",command=self.OnButtonClick)
		button.grid(column=1,row=0)
		#fg=foregorund bg = background
		#unuseful crap
		
		#usefull for outputing the info to the user
		
		label = Tkinter.Label(self,anchor="w",fg="white",bg="blue")
		label.grid(column=0,row=1,sticky='EW')
		
	def OnButtonClick(self):
		print "Yay"
	def OnPressEnter(self,event):
		print "You pressed enter!"
		
if __name__ == "__main__":
	app = mainGUI(None)
	app.title("Triage Program")
	app.mainloop()
	
	
