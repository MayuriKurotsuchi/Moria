class User :
    def __init__(self, login:str, password:str): #object constructor
        self.login : str = login #property = self.
        self.password : str = password
        self.vault : Vault = Vault()

    def check_password(self, password:str) -> bool:
        return self.password == password
    
    def __hash__(self) -> int:
        return hash(self.login)

    def modify_password(self,old_pwd:str, new_pwd:str):
        if self.check_password(old_pwd):
            self.password = new_pwd



class Vault :
    def __init__(self):
        self.items: dict[str,Item] = {}
        
    def create_item(self,name:str, website:str,login:str,password:str):
        
        
        """create an item
        params :
        name : unique name of item
        website : website
        login : login 
        password : non encrypted password
        returns
            True if success"""
        
        item = Item(name,website,login,password)
        if name not in self.items:
            self.items[name] = item
            

    def show_items(self):
        for item in self.items.values():
            print(item)

    def show_details(self,key:str):
        if key in self.items:
            print(self.items[key])
        else:
            pass#to do
    def update_item(self):
        if key in self.items:
            self.items.update()
            print(f"Item has been updated")
    def remove_item(self):
        pass
    
    def search_by_name(self):
        pass 


class Item :
    def __init__ (self, name:str, website:str, login:str, password:str):
        self.name : str = name
        self.website : str = website
        self.login : str = login
        self.password : str = password

    def __str__(self) -> str:
        return f"Name: {self.name}\nWebsite : {self.website}\nLogin: {self.login}\nPassword {self.password}"
    
    def __hash__(self) -> int:
        return hash(self.name)