import json

class DB:
    def __init__(self, db_path):
        #Initialize the database
        #Open the database file if it exists, otherwise create a new database file
        self.db_path = db_path
        try:
            with open(db_path, 'r') as f:
                self.db = json.load(f)
        except FileNotFoundError:
            self.db = {}
            #Save the database to the database file
            with open(db_path, 'w') as f:
                json.dump(self.db, f, indent=4)
    def save(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.db, f, indent=4)
        return None
    
    def starting(self,chat_id):
        self.db['users'][str(chat_id)]={'til':'uz'}
        return None
    
    def add_lang(self,lang,chat_id):
        self.db['users'][str(chat_id)]['til'] = lang
        return None
    
    def get_lang(self , chat_id):
        return self.db['users'][str(chat_id)]['til']
    
    def get_loc(self,yunalish):
        if yunalish=='tes':
            return self.db['bekatlar']["teskari"]
        else:
            return self.db['bekatlar']["to'g'ri"]
    def get_time(self,tartib,yunalish):
        return self.db['bekat'][yunalish][tartib]
    def get_admin(self):
        return self.db['admin']['admins']
    def del_admin(self,user_id):
        try:
            admins=self.db['admin']['admins']
            admins.remove(user_id)
            return True
        except:
            return False
    def add_admin(self,user_id):
        if user_id in self.db['admin']['admins']:
            return False
        else:
            admins=self.db['admin']['admins']
            admins.append(user_id)
            return True
    def get_about(self):
        return (self.db['bekat']['interval'], self.db['bekat']['start'],self.db['bekat']['end'])
    def upd(self,inter=None,start=None,end=None):
        if inter is not None:
            self.db['bekat']['interval']=inter
            return None
        elif start is not None:
            self.db['bekat']['start']=start
            return None
        elif end is not None:
            self.db['bekat']['end']=end
            return None
        