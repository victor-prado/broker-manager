import tkinter as tk
import pandas as pd
#from Data import Data
from NewClient import NewClient
from NewCorporation import NewCorporation
from SearchClient import SearchClient
from SearchDate import SearchDate
from SearchCorporation import SearchCorporation
from Dates import Reminder


def addClient():
    "Execute class NewClient"
    top = tk.Tk()
    new_client = NewClient(master=top)
    new_client.addButtons()

def addCorporation():
    "Execute class NewCorporation"
    top = tk.Tk()
    new_corporation = NewCorporation(master=top)
    new_corporation.addButtons()

def searchClient():
    "Execute class SearchClient"
    top = tk.Tk()
    client_search = SearchClient(master=top)

def searchDate():
    "Execute class searchDate"
    top = tk.Tk()
    date_search = SearchDate(master=top)
    
def editCorporation():
    "Execute class EditCorporation"
    top = tk.Tk()
    corp = SearchCorporation(master=top)

    
#data = Data()
root = tk.Tk()
menubar = tk.Menu(root)

frame1 = tk.Frame(root)
frame1.grid()

for i in range(5):
    tk.Label(frame1, text='                                                ').grid()

frame2 = tk.LabelFrame(root, text="Vencimentos")
frame2.grid()

reminder = Reminder(frame2)

addmenu = tk.Menu(menubar, tearoff=0)
addmenu.add_command(label="Novo Cliente", command=addClient)
addmenu.add_command(label="Nova Corporação", command=addCorporation)
menubar.add_cascade(label="Adicionar", menu=addmenu)

searchmenu = tk.Menu(menubar, tearoff=0)
searchmenu.add_command(label="Buscar Cliente", command=searchClient)
searchmenu.add_command(label="Buscar Datas", command=searchDate)
menubar.add_cascade(label="Consultar", menu=searchmenu)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Editar Corporação", command=editCorporation)
menubar.add_cascade(label="Editar", menu=editmenu)

root.config(menu=menubar)
root.mainloop()
#data.db.close()
