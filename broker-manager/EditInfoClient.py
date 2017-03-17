import tkinter as tk
from Data import Data

class EditInfoClient(tk.Frame):
    
    def __init__(self, master=None, id_client=None):
        super().__init__(master)
        self.id_client = id_client
        self.text = tk.Text(master)
        self.add_info()

    def add_info(self):
        labelText = tk.Label(self.master,
                           text="Informações adicionais sobre o cliente")
        labelText.grid()
        self.text.grid()

        data = Data()
        data.clientById(self.id_client)
        try:
            self.text.insert("insert", data.client[0]["info"])
        except:
            self.text.insert("insert", " ")
            
