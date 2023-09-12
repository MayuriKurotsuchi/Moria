def notice(text: str):
    print(f"Notice: {text}")

def error(text: str):
    print(f"Error: {text}")   

def warning(text: str):
    print(f"Warning: {text}") 

def create_user():
    user_login = input("Ask for a new login:")
    if user_login in users.keys():
        error("user not found?.")
    else:
        users[user_login] = []
        notice(": User created.")

def remove_user():
    user_login = input("Enter your login: ")
    if user_login in users.keys():
        confirmation = input("Sure you want to delete account ? (YES or NO): ")
        if confirmation == "YES":
            del users[user_login]
            print("notice succesfully removed")        
        else:
            error("ERROR")

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

def create_item():
# ask for informations (website, log and password)
    item_id = input("ask website: ")
    #item_login = input("ask for a login: ")
    #item_password = input("ask for a password: ")
    active_vault.append(item_id)
    print(f"Notice: {item_id}")
    

def remove_item():
    pass

def edit_item():
    pass

def list_item():
    for item in active_vault:
        item_name, item_login, item_pass = item
        print(item_name)

    pass

def show_items():
    item_name = input("Enter item's name: ")
    if item_name in active_vault:
        print(item_name)

def search_by_name():
    query = input("enter beginning of the name: ")
    for item in active_vault:
        item_name,_,_ = item
        if item_name.startswith(query):
            print(item_name)

def ask_for_number() -> int:
    choice : str = input("your choice: ")
    if choice.isdigit():
        return int(choice)
    else: 
        print("Error: Not a number")
        return -1
def main():
    print("Welcome to Gandalf!".center(100, "="))

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
                exit()
            case _:
                print("Kraken")


# Entry point
if __name__ == "__main__":
    #Some variables
    users: dict[str,list[str]] = {} #key: str, value: list of tuples
    active_vault:  list[str] = []
    main()