import random as r

class Bank:
    def __init__(self):
        self.unique_id = ''.join([str(r.randint(0,9)) for x in range(8)])
        self.dob = None
        self.creation_date = None
        self.status = None  
        self.balance = None
        
bank_dct = {}
bank_dct['unique_id'] = ''.join([str(r.randint(0,9)) for x in range(8)])
bank_dct['creation_date'] = None
bank_dct['dob'] = None
bank_dct['status'] = None
bank_dct['balance'] = None

bank_lst = [''] * 4
bank_lst[0] = ''.join([str(r.randint(0,9)) for x in range(8)])
bank_lst[1] = None
bank_lst[2] = None
bank_lst[3] = None
bank_lst[4] = None


