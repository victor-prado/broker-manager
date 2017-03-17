import pandas as pd
import numpy as np

corporation1 = {'id': 1,
				'cnpj': '00.000.000/0001-00',
				'name': 'Fake Corporation',
				'site': 'fakecorporation.com'}

corporation2 = {'id':2,
				'cnpj': 'xx.xxx.xxx/xxxx-xx',
				'name': 'Second Fake Corporation',
				'site': 'fakecorp2.com'}


Corporation1 = pd.Series(corporation1)
Corporation2 = pd.Series(corporation2)
Corporations = pd.DataFrame([Corporation1, Corporation2])

Corporations.to_csv('corporation.csv')