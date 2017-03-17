import tkinter as tk
from Data import Data
from NewCorporation import NewCorporation

class EditCorporation(tk.Frame, Data):

    def __init__(self, master=None, id_corporation=None):
        super().__init__(master)
        self.id_corporation = id_corporation
        self.corp = NewCorporation(self.master)
        self.create_table()

    def create_table(self):
        self.get_corporation(self.id_corporation)
        self.corp.E[0].put()
        self.corp.E[1].put()
        self.corp.E[2].put()

    def addButtons(self):
        tk.Button(self.master, text="Salvar", command=self.save_update).grid()

    def save_update(self):
        self.corp.E[0].catch()
        self.corp.E[1].catch()
        self.corp.E[2].catch()
        self.updateCorporation()

#root = tk.Tk()
#app = EditCorporation(master=root, id_corporation=1)
#app.addButtons()
#app.mainloop()
#data = Data()
#data.db.close()
