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