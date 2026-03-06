"""Simple Student Portal Application"""

def main():
    print("Welcome to Student Portal System")

def login(username):
    print(f"LOGIN SUCCESS: {username} has entered the system")

def logout(username):
    print(f"User {username} logged out.")

def show_menu():
    print("1. Login")
    print("2. Exit")

if __name__ == "__main__":
    main()