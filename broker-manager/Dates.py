import tkinter as tk
import datetime
from Data import Data

class Dates():

	def fromToday(_days):
		today = datetime.date.today()
		date = today + datetime.timedelta(days=_days)
		year, month, day = str(date.year), str(date.month), str(date.day)
		if len(month) == 1:
			month = '0' + month
		if len(day) == 1:
			day = '0' + day
		return year + '-' + month + '-' + day

	def isoToLocal(isodate):
		year = int(isodate[0:4])
		month = int(isodate[5:7])
		day = int(isodate[8:10])
		date = datetime.date(year, month, day)
		localdate = date.strftime('%d-%m-%Y')
		return localdate

	def localToIso(localdate):
		day = int(localdate[:2])
		month = int(localdate[3:5])
		year = int(localdate[6:])
		date = datetime.date(year, month, day)
		return date.isoformat()

from EditClient import EditClient

class Reminder(tk.Frame, Data):

	def __init__(self, master=None):
		super().__init__(master)
		self.endThisWeek()
		self.endAfterWeek()

	def endAfterWeek(self):
		for days in range(8, 365):
			#date = self.isoToLocal(self.endContract(days))
			isodate = Dates.fromToday(_days=days)
			date = Dates.isoToLocal(isodate)
			contracts = self.contractByDate(date)
			
			
			for cod in contracts:
				self.get_contract(cod)
				#self.clientByContract(str(cod[0]))
				tk.Label(self.master, text=self.contract["name"]).grid(row=line, column=0)
				tk.Button(self.master, text=date, 
					command= lambda c_id = self.contract["id_client"] : self.open_client(c_id)).grid(row=line, column=1)
				return


	def endThisWeek(self):
		color = 'red'
		global line
		line = 0
		for days in range(8):
			#date = self.isoToLocal(self.endContract(days))
			isodate = Dates.fromToday(_days=days)
			date = Dates.isoToLocal(isodate)
			contracts = self.contractByDate(date)			
			for cod in contracts:
				self.get_contract(cod)
				#self.clientByContract(str(cod[0]))
				tk.Label(self.master, text=self.contract["name"], fg=color).grid(row=line, column=0)
				tk.Button(self.master, text=date, 
					command= lambda c_id = self.contract["id_client"] : self.open_client(c_id), fg=color).grid(row=line,column=1)
				line += 1
			color='orange'
			
	def open_client(self, id_client):
		top = tk.Tk()
		client = EditClient(top, id_client)
		client.addButtons()

#top = tk.Tk()
#app = Warning(top)
#top.mainloop()
#data = Data()
#data.db.close()