def create_user():
    user_login = input("Ask for a new login:")
    if user_login in users.keys():
        print(" user already exists ERROR")
    else:
        users[user_login] = []
        print("notice: User created.")

def remove_user():
    pass


def login():
    pass


def create_item():
    pass


def remove_item():
    pass


def list_item():
    pass


def show_items():
    pass


def search_items():
    pass


def list_items():
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
              
              >r0 Exit
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
    
    main()
