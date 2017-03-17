import tkinter as tk
from Data import Data
from EditClient import EditClient

class Client(tk.Frame):

    def __init__(self, master=None, client_id=None):
        super().__init__(master)
        self.id = client_id
        self.create_table()

    def create_table(self):
        global data
        data = Data()
        data.clientById(self.id)
        data.contractByClient(self.id)
    
        label1 = tk.Label(self.master,
                          text=data.client[0]["name"])
        label1.grid(row=0, column=0)
        label2 = tk.Label(self.master,
                          text="rg: "+data.client[0]["rg"])
        label2.grid(row=1, column=0)
        label3 = tk.Label(self.master,
                          text="gênero: "+data.client[0]["gender"])
        label3.grid(row=2, column=0)
        label4 = tk.Label(self.master,
                          text="nascimento: "+data.client[0]["born"])
        label4.grid(row=3, column=0)
        labelframe1 = tk.LabelFrame(self.master,
                          text="Informações adicionais")
        
        labelframe1.grid(row=0, column=1)
        label5 = tk.Label(labelframe1, text=data.client[0]["info"])
        label5.grid()

        labelframe2 = tk.LabelFrame(self.master, text="Contratos")
        labelframe2.grid(row=4, column=0)
        for line in data.contract:
            label6 = tk.Label(labelframe2, text=data.contract[0]["name"])
            label6.grid()
        if(data.contract[0]["price"]=="None"):
            label7 = tk.Label(labelframe2, text=data.contract[0]["monthly_price"])
            label7.grid(row=1, column=0)
        else:
            label7 = tk.Label(labelframe2, text=data.contract[0]["price"])
            label7.grid(row=1, column=0)
        label8 = tk.Label(labelframe2, text=data.contract[0]["start"] +\
                          " até " + data.contract[0]["end"])
        label8.grid(row=2, column=0)
        button1 = tk.Button(self.master, text="Editar", command=self.edit_client)
        button1.grid()

    def edit_client(self):
        root = tk.Tk()
        edit = EditClient(master=root, id_client=data.client[0]["id"])
        edit.addButtons()

#root = tk.Tk()
#app = Client(root, 1)
#app.mainloop()
#data = Data()
#data.db.close()
        
