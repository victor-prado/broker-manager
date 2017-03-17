import tkinter as tk
from Data import Data
from BindEntry import BindEntry

class NewCorporation(tk.Frame, Data):

    def __init__(self, master=None):
        super().__init__(master)
        self.clear(self.corporation)
        self.E = []        
        self.E.append(BindEntry(self.master, self.corporation, "name", "Nome"))
        self.E.append(BindEntry(self.master, self.corporation, "site", "Site"))
        self.E.append(BindEntry(self.master, self.corporation, "cnpj", "CNPJ"))
        self.create_table()

    def create_table(self):
        self.E[0].label.grid(row=0, column=0)
        self.E[0].entry.grid(row=0, column=1)
        self.E[1].label.grid(row=1, column=0)
        self.E[1].entry.grid(row=1, column=1)
        self.E[2].label.grid(row=2, column=0)
        self.E[2].entry.grid(row=2, column=1)

    def addButtons(self):        
        tk.Button(self.master, text="Salvar", command=self.save_corp).grid()

    def save_corp(self):
        self.E[0].catch()
        self.E[1].catch()
        self.E[2].catch()
        self.saveCorporation()



#root = tk.Tk()
#app = NewCorporation(master=root)
#app.addButtons()
#app.mainloop()
