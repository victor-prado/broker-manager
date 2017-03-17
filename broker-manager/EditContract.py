from Data import Data
import tkinter as tk
from NewContract import NewContract

class EditContract(tk.Frame, Data):

	def __init__(self, master=None, id_contract=None):
		super().__init__(master)
		self.id_contract = id_contract
		self.nc = NewContract(master=self.master)
		self.write_entry()

	def write_entry(self):
		self.get_contract(self.id_contract)
		for ent in self.nc.E:
			ent.put()
		self.get_corporation(self.contract["id_corporation"])
		self.nc.box.insert("insert", self.corporation["name"])

#top = tk.Tk()
#app = EditContract(master=top, id_contract="2")
#app.mainloop()
#data = Data()
#data.db.close()
