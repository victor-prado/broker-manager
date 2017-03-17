import tkinter as tk
from tkinter import ttk
from Data import Data
from BindEntry import BindEntry

class NewContract(tk.Frame, Data):

    def __init__(self, master=None, id_client=None):
        super().__init__(master)
        self.E = []
        for i in range(5):
            self.E.append(0)

        self.E[0] = BindEntry(self.master, self.contract, "name", "Nome")
        self.E[1] = BindEntry(self.master, self.contract, "monthly_price", "Valor Mensal")
        self.E[2] = BindEntry(self.master, self.contract, "price", "Valor Absoluto")
        self.E[3] = BindEntry(self.master, self.contract, "start", "Inicio do Contrato")
        self.E[4] = BindEntry(self.master, self.contract, "end", "Fim do Contrato")
        self.box = ttk.Combobox(self.master)
        self.used = False
        self.id_client = id_client
        #self.contract = []
        #self.clear_contract()
        self.create_table()
        

    #def create_entry(self, row_value, message):       
    #    L = tk.Label(self.master, text=message)
    #    E = tk.Entry(self.master, bd=5)
    #    return (L,E)

    def create_table(self):

        self.E[0].label.grid(row=0, column=0)
        self.E[0].entry.grid(row=0, column=1)
        self.E[1].label.grid(row=2, column=0)
        self.E[1].entry.grid(row=2, column=1)
        self.E[2].label.grid(row=3, column=0)
        self.E[2].entry.grid(row=3, column=1)
        self.E[3].label.grid(row=4, column=0)
        self.E[3].entry.grid(row=4, column=1)
        self.E[4].label.grid(row=5, column=0)
        self.E[4].entry.grid(row=5, column=1)
        
        F1 = tk.Label(self.master, text="Corporação", bd=5)
        F1.grid(row=1, column=0)
        #ids = self.allCorporation()
        #corp=[]
        #for corp_name in corporation['name']:
            #self.corporationById(str(id[0]))
            #corp.append(corp_name)
        
        self.box["values"] = list(self.corporation_table['name'])
        self.box.grid(row=1, column=1)

        #tirar, e colocar numa função a parte

    def addButtons(self):
        tk.Button(self.master, text="Salvar", command=self.save_contract).grid()

    def defautValues(self):
        self.E[1].entry.insert("insert", "0.00")
        self.E[2].entry.insert("insert", "0.00")

    def save_contract(self):
        self.contract["id_client"] = self.id_client
        name = self.box.get()
        self.corporationByName(name)
        self.contract["id_corporation"] = self.corporation["id"]
        for entry in self.E:
            entry.catch()
        #self.contract["name"] = self.E1[1].get()
        #self.contract["monthly_price"] = self.E2[1].get()
        #self.contract["price"] = self.E3[1].get()
        #self.contract["start"] = self.E4[1].get()
        #self.contract["end"] = self.E5[1].get()
        #self.used = True
        #print(self.contract)


        

#app = NewContract(master=root)
#app.mainloop()
