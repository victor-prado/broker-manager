import pandas as pd
import numpy as np

client1 = {'id': 1, 
		   'name': 'Cliente Falso',
		   'rg': 'xxx.xxx.xxx-x', 
 		   'gender': 'F', 
 		   'born': '23-07-1990',
  		   'info': 'Este cliente não é real', 
		   'cpf': 'xxx.xxx.xxx-xx', 
		   'status': 'solteiro(a)',
           'state': 'SP', 
           'city': 'São Paulo', 
           'neigh': 'Vila Mariana', 
           'adress': 'Autódromo', 
           'num': 300, 
           'comp': np.nan, 
           'cep': 'xxx.xxx', 
           'tel1': '(xx)xxxx-xxxx',
           'tel2': np.nan, 
           'email': 'falso.cliente@broker.com'}

client2 = {'id': 2, 
		   'name': 'Cliente Falso 2',
		   'rg': 'xxx.xxx.xxx-x', 
 		   'gender': 'M', 
 		   'born': '23-07-1992',
  		   'info': 'Este cliente não é real', 
		   'cpf': 'xxx.xxx.xxx-xx', 
		   'status': 'solteiro(a)',
           'state': 'SP', 
           'city': 'São Paulo', 
           'neigh': 'Vila Mariana', 
           'adress': 'Autódromo', 
           'num': 301, 
           'comp': np.nan, 
           'cep': 'xxx.xxx', 
           'tel1': '(xx)xxxx-xxxx',
           'tel2': np.nan, 
           'email': 'falso.cliente2@broker.com'}

Client1 = pd.Series(client1)
Client2 = pd.Series(client2)

Clients = pd.DataFrame([Client1, Client2])
Clients.to_csv('client.csv')
