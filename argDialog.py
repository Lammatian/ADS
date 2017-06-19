from tkinter import *
import tkSimpleDialog

class ArgDialog(tkSimpleDialog.Dialog):

	def body(self, master):
		"""Body of the dialog with entries for all arguments"""
		for i, arg in enumerate(self.args):
			Label(master, text=(arg + " ")).grid(row=i)

		self.entries = [None]*len(self.args)

		for i in range(len(self.args)):
			self.entries[i] = Entry(master)

		for i, entry in enumerate(self.entries):
			entry.grid(row=i, column=1)

		return self.entries[0] # initial focus


	def apply(self):
		# TODO - change to do right thing preferably
		self.result = [s.get() for s in self.entries]