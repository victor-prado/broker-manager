import tkinter as tk
from NewInfoClient import NewInfoClient
from NewContract import NewContract
from Data import Data
from BindEntry import BindEntry


class NewClient(tk.Frame, Data):

    def __init__(self, master=None):
        super().__init__(master)
        self.E = []
        for i in range(17):
            self.E.append((1,1))
        self.E[0] = BindEntry(self.master, self.client, "name", "Nome Completo")
        self.E[1] = BindEntry(self.master, self.client, "rg", "RG")
        self.E[2] = BindEntry(self.master, self.client, "gender", "Gênero")
        self.E[3] = BindEntry(self.master, self.client, "born", "Nascimento")
        self.E[5] = BindEntry(self.master, self.client, "cpf", "CPF")
        self.E[6] = BindEntry(self.master, self.client, "status", "Estado Civil")
        self.E[7] = BindEntry(self.master, self.client, "state", "Estado")
        self.E[8] = BindEntry(self.master, self.client, "city", "Cidade")
        self.E[9] = BindEntry(self.master, self.client, "neigh", "Bairro")
        self.E[10] = BindEntry(self.master, self.client, "adress", "Endereço")
        self.E[11] = BindEntry(self.master, self.client, "num", "Número")
        self.E[12] = BindEntry(self.master, self.client, "comp", "Complemento")
        self.E[13] = BindEntry(self.master, self.client, "cep", "CEP")
        self.E[14] = BindEntry(self.master, self.client, "tel1", "Telefone 1")
        self.E[15] = BindEntry(self.master, self.client, "tel2", "Telefone 2")
        self.E[16] = BindEntry(self.master, self.client, "email", "E-mail")
        #self.clear_client()
        #self.clear_contract()

        #id of the current client
        global cur_id 
        index = self.client_table.index
        cur_id = index.max() + 1 

        self.create_table()

    def create_entry(self, message):       
        L = tk.Label(self.master, text=message, justify="left")
        #L.grid(row=row_value, column=0)
        E = tk.Entry(self.master, bd=5)
        #E.grid(row=row_value, column=1)
        return (L, E)

    def create_table(self):
        self.E[0].label.grid(row=0, column=0)
        self.E[0].entry.grid(row=0, column=1)
        self.E[1].label.grid(row=1, column=0)
        self.E[1].entry.grid(row=1, column=1)
        self.E[2].label.grid(row=2, column=0)
        self.E[2].entry.grid(row=2, column=1)
        self.E[3].label.grid(row=3, column=0)
        self.E[3].entry.grid(row=3, column=1)
        self.E[5].label.grid(row=4, column=0)
        self.E[5].entry.grid(row=4, column=1)
        self.E[6].label.grid(row=5, column=0)
        self.E[6].entry.grid(row=5, column=1)
        self.E[7].label.grid(row=6, column=0)
        self.E[7].entry.grid(row=6, column=1)
        self.E[8].label.grid(row=7, column=0)
        self.E[8].entry.grid(row=7, column=1)
        self.E[9].label.grid(row=8, column=0)
        self.E[9].entry.grid(row=8, column=1)
        self.E[10].label.grid(row=9, column=0)
        self.E[10].entry.grid(row=9, column=1)
        self.E[11].label.grid(row=10, column=0)
        self.E[11].entry.grid(row=10, column=1)
        self.E[12].label.grid(row=11, column=0)
        self.E[12].entry.grid(row=11, column=1)
        self.E[13].label.grid(row=12, column=0)
        self.E[13].entry.grid(row=12, column=1)
        self.E[14].label.grid(row=13, column=0)
        self.E[14].entry.grid(row=13, column=1)
        self.E[15].label.grid(row=14, column=0)
        self.E[15].entry.grid(row=14, column=1)
        self.E[16].label.grid(row=15, column=0)
        self.E[16].entry.grid(row=15, column=1)
        
    def addButtons(self):
        tk.Button(self.master,
                  text="Informações adicionais",
                  command=self.add_info).grid(row=17, column=1, columnspan=1)
        tk.Button(self.master,
                  text="Adicionar Contrato",
                  command=self.add_contract).grid(row=18, column=1)
        tk.Button(self.master, text="Salvar",
                  command=self.save_on_db).grid(row=18, column=0)
        #tk.Button(self.master, text="Show",
         #          command=self.show).grid()
    
    def add_info(self):
        textRoot = tk.Tk()
        info = NewInfoClient(master=textRoot)
        return info

    def add_contract(self):
        contractRoot = tk.Tk()
        global contract
        contract = NewContract(master=contractRoot, id_client=cur_id)
        contract.defautValues()
        contract.addButtons()

    def save_on_db(self):
        self.E[0].catch()
        self.E[1].catch()
        self.E[2].catch()
        self.E[3].catch()
        self.E[5].catch()
        self.E[6].catch()
        self.E[7].catch()
        self.E[8].catch()
        self.E[9].catch()
        self.E[10].catch()
        self.E[11].catch()
        self.E[12].catch()
        self.E[13].catch()
        self.E[14].catch()
        self.E[15].catch()
        self.E[16].catch()               
        #self.setNullClient()
        #print(self.client)
        self.saveClient() 
        if (self.contract["id_client"] == cur_id):
        	self.saveContract()
            #print(self.contract)

    #def show(self):
     #   print(self.client)
      #  print(self.contract)
        
        
#root = tk.Tk()
#app = NewClient(master=root)
#app.addButtons()
#app.mainloop()
        
