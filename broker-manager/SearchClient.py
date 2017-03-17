import tkinter as tk
from Data import Data
from EditClient import EditClient

class SearchClient(tk.Frame, Data):

    def __init__(self, master=None):
        super().__init__(master)
        self.frame = tk.Frame(self.master)
        self.E1 = self.create_entry(0, "Nome")
        self.create_table()

    def create_entry(self, row_value, message):       
        L = tk.Label(self.master, text=message)
        #L.grid(row=row_value, column=0)
        E = tk.Entry(self.master, bd=5)
        #E.grid(row=row_value, column=1)
        return (L,E)

    def create_table(self):
        
        self.E1[0].grid(row=0, column=0)
        self.E1[1].grid(row=0, column=1)
        B1 = tk.Button(self.master, text="Buscar",
                       command=self.search_client)
        B1.grid(row=0, column=2)

    def search_client(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.master)
        self.frame.grid()
        ids = self.client_table[self.client_table['name'] == self.E1[1].get()].index
        for ind in ids:
            self.get_client(ind)
            result = self.client["name"] + " | " + self.client["rg"]
            tk.Button(self.frame, text=result, 
                      command= lambda current_id=ind : self.open_client(current_id)).grid()

    def open_client(self, id_client):
        top = tk.Tk()
        edit_client = EditClient(master=top, id_client=id_client)
        edit_client.addButtons()
        

        
    
#root = tk.Tk()
#app = SearchClient(master=root)
#app.mainloop()

