class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedIn = False
        self.menu()
    def menu(self):
        user_input = input("Welcome to Chatbook! Please select an option:\n1. Signup\n2. Signin\n3. Write a Post\n4. Message a friend\n5. Exit\n")
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
            
if __name__ == "__main__":
    chatbook()