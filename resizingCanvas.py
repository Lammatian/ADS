import tkinter as tk

class ResizingCanvas(tk.Canvas):
	"""
	A subclass of Canvas for dealing with resizing windows
	Taken from https://stackoverflow.com/questions/22835289/how-to-get-tkinter-canvas-to-dynamically-resize-to-window-width
	"""
	def __init__(self, parent, **kwargs):
		tk.Canvas.__init__(self, parent, **kwargs)
		self.bind("<Configure>", self.on_resize)
		self.height = self.winfo_reqheight()
		self.width = self.winfo_reqwidth()


	def on_resize(self, event):
		"""Resize all elements of canvas on resize of the window"""
		# determine the ratio of old width/height to new values
		wscale = float(event.width)/self.width
		hscale = float(event.height)/self.height
		self.width = event.width
		self.height = event.height
		# resize the canvas
		self.config(width=self.width, height=self.height)
		# resize all the objects tagged with "all" tag (by addtag_all method)
		self.scale("all", 0, 0, wscale, hscale)

def main():
	root = tk.Tk()
	myframe = tk.Frame(root)
	myframe.pack(fill="both", expand="yes")
	mycanvas = ResizingCanvas(myframe, width=850, height=400, bg="white", highlightthickness=0)
	mycanvas.pack(fill="both", expand="yes")

	mycanvas.create_line(0, 0, 200, 100)
	mycanvas.create_line(0, 100, 200, 0, fill="red", dash=(4,4))
	mycanvas.create_rectangle(50, 25, 150, 75, fill="blue")

	mycanvas.addtag_all("all")
	root.mainloop()

if __name__ == "__main__":
	main()