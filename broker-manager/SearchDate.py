import tkinter as tk
from Data import Data
from EditClient import EditClient

class SearchDate(tk.Frame, Data):

    def __init__(self, master=None):
        super().__init__(master)
        self.frame = tk.Frame(self.master)
        self.frame.grid()
        self.create_table()

    def create_entry(self, row_value, message):       
        L = tk.Label(self.master, text=message)
        L.grid(row=row_value, column=0)
        E = tk.Entry(self.master, bd=5)
        E.grid(row=row_value, column=1)
        return E

    def create_table(self):
        global E1
        E1 = self.create_entry(0, "Data")
        B1 = tk.Button(self.master, text="Buscar",
                       command=self.search_date)
        B1.grid(row=0, column=2)

    def search_date(self):
        parameter = E1.get()
        ids = self.contractByDate(parameter)
        #print(ids)            
        self.frame.destroy()
        self.frame = tk.Frame(self.master)
        self.frame.grid()
        i=0
        for line in ids:
            self.get_contract(line)
            self.get_client(self.contract["id_client"])
            try:
                result = self.client["name"]
                
            except:
                result = "(Sem nome)"
                
            button = tk.Button(self.frame, text=result,
                               command= lambda id_client = self.client["id"]:
                               self.open_client(id_client))
            button.grid()
            i=i+1

    def open_client(self, id_client):
        top = tk.Tk()
        client = EditClient(master=top, id_client=id_client)
        client.addButtons()

#Arrumar!

#root = tk.Tk()
#app = SearchDate(master=root)
#app.mainloop()
#data = Data()
#data.db.close()
