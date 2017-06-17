from tkinter import *
import os

class Dialog(Toplevel):
	"""Taken from http://effbot.org/tkinterbook/tkinter-dialog-windows.htm"""

	def __init__(self, parent, args, title=None):

		self.args = args

		Toplevel.__init__(self, parent)
		# associate the dialogue with application
		self.transient(parent)

		if title:
			self.title(title)

		self.parent = parent

		self.result = None

		body = Frame(self)
		self.initial_focus = self.body(body)
		body.pack(padx=5, pady=5)

		# add buttons
		self.buttonbox()

		# all events can happen only in this window
		self.grab_set()

		if not self.initial_focus:
			self.initial_focus = self

		# so that you can cancel the dialogue
		self.protocol("WM_DELETE_WINDOW", self.cancel)

		# set dialogue to be in the middle of the app
		self.geometry("+{}+{}".format(parent.winfo_rootx()+parent.winfo_width()//3, parent.winfo_rooty()+parent.winfo_height()//2))

		# set focus of keyboard to dialogue
		self.initial_focus.focus_set()

		# don't let anything happen in main application
		self.wait_window(self)


	def body(self, master):
		# create a dialog body. return widged that should have
		# initial focus. this method should be overwritten
		pass


	def buttonbox(self):
		# add standard button box. override if you don't want the
		# standard buttons
		box = Frame(self)

		w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
		w.pack(side=LEFT, padx=5, pady=5)
		w = Button(box, text="Cancel", width=10, command=self.cancel)
		w.pack(side=LEFT, padx=5, pady=5)

		self.bind("<Return>", self.ok)
		self.bind("<Escape>", self.cancel)

		box.pack()


	def ok(self, event=None):
		"""On clicking ok button or pressing enter accept changes"""
		if not self.validate():
			self.initial_focus.focus_set()
			return

		self.withdraw()
		self.update_idletasks()

		self.apply()

		self.cancel()


	def cancel(self, event=None):
		"""put focus back to the parent window"""
		self.parent.focus_set()
		self.destroy()


	def validate(self):
		return 1 # override


	def apply(self):
		pass # override