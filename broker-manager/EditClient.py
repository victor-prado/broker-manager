import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from EditInfoClient import EditInfoClient
from NewInfoClient import NewInfoClient 
from NewContract import NewContract
from EditContract import EditContract
from NewClient import NewClient
from Data import Data
import pandas as pd

class EditClient(tk.Frame, Data):

    def __init__(self, master=None, id_client=None):
        super().__init__(master)
        self.id_client = id_client
        self.nc = NewClient(master=self.master)
        #print(self.nc.E[0].key)
        #print(self.client_table.loc[id_client])
        self.get_client(id_client)
        
        self.write_entry()
        self.create_table()

    def create_table(self):
        global fl, nameid, box
        fl = tk.LabelFrame(self.master, text="Contratos")
        fl.grid(row=17,column=0)
        contracts = self.contractByClient(self.id_client)
        name = []
        nameid = {}
        for line in contracts:
            self.get_contract(line)
            name.append(self.contract["name"])
            nameid[self.contract["name"]] = self.contract["id"]
        box = ttk.Combobox(fl)
        box["values"] = name
        box.grid(row=0, column=0)
        tk.Button(fl, text="Ver", command=self.see_contract).grid()

    def see_contract(self):
        cont_id = nameid[box.get()]
        cont_top = tk.Tk()
        edit_cont = EditContract(master=cont_top, id_contract=cont_id)
        
    def write_entry(self):
        #print(self.nc.E[0].key)
        i=0
        while i < len(self.nc.E):
            if i != 4:
                self.nc.E[i].put()
            i+=1

    def edit_info(self):
        info = self.nc.add_info()
        info.text.insert("1.0", self.nc.client["info"])

    def addButtons(self):
        tk.Button(self.master, text="informações adicionais",
                  command=self.edit_info).grid(row=18, column=1)
        tk.Button(self.master, text="Adicionar Contrato",
                  command=self.add_contract).grid(row=19, column=1)
        tk.Button(self.master, text="Salvar",
                  command=self.save_update, fg="blue").grid(row=19, column=0)
        tk.Button(self.master, text="Deletar Cliente",
                  command=self.delete_client, fg="red").grid(row=17, column=1)

    def add_contract(self):
        contractRoot = tk.Tk()
        contract = NewContract(master=contractRoot, id_client=self.nc.client["id"])
        contract.addButtons()
        contract.defautValues()

    def delete_client(self):
        asw = messagebox.askyesno("Deletar", "Você deseja deletar este cliente?")
        if (asw):
            self.deleteContractByClient()
            self.deleteClient()
            self.master.destroy()


    def save_update(self):
        i=0
        while i < len(self.nc.E):
            if i != 4:
                self.nc.E[i].catch()
            i+=1
        self.updateClient() 
        self.saveContract()
        #self.teste()

#root=tk.Tk() 
#app = EditClient(master=root, id_client=1)
#app.addButtons()
#app.mainloop()
#data = Data()
#data.db.close()
        
