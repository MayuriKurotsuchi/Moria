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
        #global active_vault
        active_vault = users[login]
        # show_menu()
    

def create_item():
    


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
    pass


def search_items():
    pass


def list_items():
    query = input("enter beginning of the name: ")
    for item in active_vault:
        item_name,_,_ = item
        
    pass


def search_by_name():
    pass

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
    users: dict[str,list[tuple[str,str,str]]] = {} #key: str, value: list of tuples
    active_vault:  list[tuple[str,str,str]] = []
    main()
