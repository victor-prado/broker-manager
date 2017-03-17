import tkinter as tk
from tkinter import ttk

class BindEntry():

	def __init__(self, master, key, index, labelText, entity="entry"):
		self.key = key
		self.index = index
		self.label = tk.Label(master, text=labelText)
		if entity == "entry":
			self.entry = tk.Entry(master, bd=5)
		if entity == "box":
			self.entry = ttk.Combobox(self.master)

	def catch(self):
		"Atribui um novo valor a chave entrelaçada"
		self.key[self.index] = self.entry.get()

	def put(self):
		"Insert the content of the key anexade into entry"
		value = self.key[self.index]
		self.entry.insert("insert", value)
	





