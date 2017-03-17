import tkinter as tk
from Data import Data

class NewInfoClient(tk.Frame, Data):

    def __init__(self, master=None):
        super().__init__(master)
        self.text = tk.Text(master)
        self.add_info()

    def add_info(self):
        labelText = tk.Label(self.master,
                           text="Informações adicionais sobre o cliente")
        labelText.grid()
        self.text.grid()
        tk.Button(self.master, text="Pronto", command=self.save_info).grid()

    def save_info(self):
        result = self.text.get(1.0, "end")
        self.client["info"] = result
        #print(result)

#root = tk.Tk()
#app = NewInfoClient(master=root)
#app.mainloop()
