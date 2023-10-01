import os
import pickle

from colorama import Fore, Style, init  #vice versa ligne 1&2


def save():
    with open("data.dat","wb", encoding="utf8") as file: # polisse les accents etc
        pickle.dump(users,file)


def load() -> dict:
    if os.path.exists("data.dat"):
        with open("data.dat","rb",encoding="utf8") as file:
            return pickle.load(file)
    else:
        return {}


# Define functions for notices, errors and warnings
def notice(text: str):
    print(Fore.LIGHTBLUE_EX +f"Notice: {text}")

def error(text: str):
    print(Fore.LIGHTRED_EX + f"Error: {text}")   

def warning(text: str):
    print(Fore.LIGHTYELLOW_EX + f"Warning: {text}") 

# function to create new user account
def create_user():
    user_login = input("Ask for a new login:")
    if user_login in users.keys():
        error("user not found?.")
    else:
        users[user_login] = []
        notice(": User created.")

# function to create a new user account
def remove_user():
    user_login = input("Enter your login: ")
    if user_login in users.keys():
        confirmation = input("Sure you want to delete account ? (YES or NO): ")
        if confirmation == "YES":
            del users[user_login]
            notice("Succesfully removed")        
        else:
            error("ERROR")

# Function for user login
def login():
    #ask user name
    #verify existensy in in data
    #get associated vault
    #show new menu
    login = input("Ask user name: ")
    if login in users:
        global active_vault
        active_vault = users[login]
        show_menu()

# Function to define the main menu  
def show_menu():
    print("Menu".center(100,"="))
    
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

        choice = ask_for_number() #int(input("Your choice: "))

        match choice:
            case 1:
                create_item()
            case 2:
                remove_item()
            case 3:
                edit_item()
            case 4:
                list_item()
            case 5:
                show_items()
            case 6:
                search_by_name()
            case 0:
                save()
                exit()
            case _:
                print("Error")

# Function to create a new  item in vault
def create_item():
# ask for informations (website, log and password)
    item_id = input("ask item name: ")
    item_website = ("Ask website:")
    #item_login = input("ask for a login: ")
    #item_password = input("ask for a password: ")
    active_vault.append(item_id)
    notice(f" {item_id}")
    
# function to remove an item in vault
def remove_item():
    item_name = input("Enter item name: ")
    if item_name in active_vault:
        active_vault.remove(item_name)
        notice(f"Item {item_name} remove done.")
    else:
        error(f"Item {item_name} not found in vault.")


    
# Function to edit item in the vault
def edit_item():
    item_name = input("Enter item name: ")
    if item_name in active_vault:
        active_vault.remove(item_name)
        new_item_name = input("Enter the new item name: ")
        active_vault.append(new_item_name)
        print("Item edited successfully.")
    else:
        print("Item not found in the vault.")
        
        
# function to list items in the vault
def list_item():
    for item in active_vault:
        item_name, item_login, item_pass = item
        notice(item_name)

    
# Function to show items detail in the vault
def show_items():
    item_name = input("Enter item's name: ")
    if item_name in active_vault:
        print(item_name)

# function to search item by name in the vault
def search_by_name():
    query = input("enter beginning of the name: ")
    for item in active_vault:
        item_name,_,_ = item
        if item_name.startswith(query):
            print(item_name)

# Function to ask the user for number input
def ask_for_number() -> int:
    choice : str = input("your choice: ")
    if choice.isdigit():
        return int(choice)
    else: 
        print("Error: Not a number")
        return -1

# main program entry point
def main():
    print(Style.BRIGHT + "Welcome to Gandalf!".center(100, "="))

    choice : int = -1 !=0 #eqv to choice int = -1

    while choice != 0 : 
        print("""
            \r1 Create user
            \r2 Remove user
            \r3 login
            
            \r0 Exit
            """)
        
        choice = ask_for_number() #int(input("Your choice: "))

        match choice:
            case 1: 
                create_user()
            case 2:
                remove_user()
            case 3:
                login()
            case 0:
                save()
                exit()
            case _:
                print("Error")


# Entry point for user and vault data
if __name__ == "__main__":
    #Some variables
    init(autoreset=True)

    users: dict[str,list[str]] = load() #key: str, value: list of tuples
    active_vault:  list[str] = []
    main()