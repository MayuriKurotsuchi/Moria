import os, pickle
from colorama import Fore, Style, init
from data import User, Vault


class App:
    active_user: User
    def __init__(self) -> None:
        init(autoreset=True) #colorama
        self.users: dict[User,Vault] = self.load() # function load send a dictionary
        
        self.main()

    def load(self) -> dict[User,Vault]:
        
    def save(self):
        pass

    def main(self):
        pass
    
    @staticmethod
    def error(text:str):
        print(Fore.LIGHTRED_EX + f"Error: {text}")

    def notice(self, text: str):


    def warning(self, text:str):
        pass

    def ask_for_number(self) -> init
    pass

    def create_user(self):
        pass

    def login(self):
        pass

    def remove_user(self):
        pass
    
    def vault_menu(self):
        """
        vault menu
        """
    
        print(Style.BRIGHT + f"{self.active_user.login}'s Vault .center(100,"°"))
    
        choice : int = -1 !=0 #eqv to choice int = -1
    
        while choice !=0 :
            print("""
                \r1 Create item
                \r2 Remove item
                \r3 Edit item
                \r4 List item
                \r5 Show item
                \r6 Search item by name
                    """)

            choice = self.ask_for_number() #int(input("Your choice: "))

            match choice:
            case 1:
                    create_item()
                case 2:
                    remove_item()
                case 3:
                    edit_item()
                case 4:
                    self.list_item()
                case 5:
                    self.users[self.active_user].show_items()
                case 6:
                    search_by_name()
                    name = input
                case 0:
                    return
                
                case _:
                    print("Error")


if __name__ == "__main__":
    app = App()
    app.main()

