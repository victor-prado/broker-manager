import tkinter as tk
from Data import Data
from EditCorporation import EditCorporation

class SearchCorporation(tk.Frame, Data):

    def __init__(self, master=None):
        super().__init__(master)        
        self.frame = tk.Frame(self.master)
        self.frame.grid()
        self.search_corp()

    def search_corp(self):
        ids = self.corporation_table.index
        #F1 = self.frame
        for line in ids:
            self.get_corporation(line)
            tk.Button(self.master, text=self.corporation["name"],
                      command= lambda id_corp = self.corporation["id"]:
                      self.open_corporation(id_corp)).grid(columnspan=2)

    def open_corporation(self, corporation_id):
        top = tk.Tk()
        corp = EditCorporation(master=top,id_corporation=corporation_id)
        corp.addButtons()

#root = tk.Tk()
#app = SearchCorporation(master=root)
#app.mainloop()
#data = Data()
#data.db.close()
