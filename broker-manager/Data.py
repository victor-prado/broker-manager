import pandas as pd 
import numpy as np 

class Data():
    "Class for manage the data base"

    client_table = pd.read_csv('./DataBase/client.csv').set_index('id')
    corporation_table = pd.read_csv('./DataBase/corporation.csv').set_index('id')
    contract_table = pd.read_csv('./DataBase/contract.csv').set_index('id')
    
    client = pd.Series([np.nan]*18, index= ['adress', 'born', 'cep', 'city', 'comp', 'cpf', 'email', 'gender', 
                                           'id', 'info', 'name', 'neigh', 'num', 'rg', 'state', 'status', 'tel1', 'tel2'])
    corporation = pd.Series([np.nan]*4, index = ['cnpj', 'id', 'name', 'site'])
    contract = pd.Series([np.nan]*7, index= ['end', 'id', 'id_client', 'id_corporation', 'monthly_price', 'name', 'price,start'])
    #Lembrete 20/02: estou com um pepino. Minhas classes redefinem os atributos de Data e isso os desatrela das BindEntry


    def saveClient(self):
        self.client_table.append(self.client)
        self.client_table.to_csv('./DataBase/client.csv')

    def saveCorporation(self):
        self.corporation_table.append(self.corporation)
        self.corporation_table.to_csv('./DataBase/corporation.csv')

    def saveContract(self):
        self.contract_table.append(self.contract)
        self.contract_table.to_csv('./DataBase/contract.csv')

    def get_client(self, id_client):
        self.client['id'] = id_client
        self.receive(self.client, self.client_table.loc[id_client])

    def get_corporation(self, id_corp):
        self.corporation['id'] = id_corp
        self.receive(self.corporation, self.corporation_table.loc[id_corp])

    def get_contract(self, id_contract):
        self.contract['id'] = id_contract
        self.receive(self.contract, self.contract_table.loc[id_contract])

    def receive(self, serie, new_serie):
        for ind in new_serie.index:
            serie[ind] = new_serie[ind]
    
    def corporationByName(self, corp_name):
        local_corp = self.corporation_table[self.corporation_table['name'] == corp_name]
        self.receive(self.corporation, local_corp)

    def clear(self, serie):
        for ind in serie.index:
            serie[ind] = np.nan

    def contractByClient(self, client_id):
        return self.contract_table[self.contract_table['id_client'] == client_id].index

    def contractByDate(self, date, event='end'):
        return self.contract_table[self.contract_table[event] == date].index        

    def deleteContractByClient(self):
        index = self.contract_table[self.contract_table['id_client'] == self.client['id']].index
        self.contract_table.drop(index)
        self.contract_table.to_csv('./DataBase/contract.csv')
        self.clear(self.contract)

    def deleteClient(self):
        self.contract_table.drop(self.client['id'])
        self.contract_table.to_csv('./DataBase/contract.csv')

    def updateClient(self):
        self.client_table.loc[self.client['id']] = self.client
        self.client_table.to_csv('./DataBase/client.csv')

    def updateCorporation(self):
        self.corporation_table.loc[self.corporation['id']] = self.corporation
        self.corporation_table.to_csv('./DataBase/corporation.csv')

