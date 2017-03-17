import pandas as pd 
import numpy as np

contract1 = {'id': 1,
			 'id_client': 1,
			 'id_corporation': 1,
			 'monthly_price': 200.00,
			 'price': 0.0,
			 'start':'23-07-2016',
			 'end': '23-07-2017',
			 'name': 'seguro falso'}

contract2 = {'id': 2,
			 'id_client': 2,
			 'id_corporation': 2,
			 'monthly_price': 0.0,
			 'price': 1700.00,
			 'start': '02-02-2015',
			 'end': '05-05-2017',
			 'name': 'Seguro auto falso'}

Contract1 = pd.Series(contract1)
Contract2 = pd.Series(contract2)
Contracts = pd.DataFrame([Contract1, Contract2])

Contracts.to_csv('contract.csv')