class chatbook:
    __user_id = 1
    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id   += 1
        self.__name = "Default user"
        self.username = None
        self.password = None
        self.loggedIn = False
        # self.menu()
    @staticmethod
    def get_id():
        return chatbook.__user_id
    @staticmethod
    def set_id(id):
        chatbook.__user_id = id
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def menu(self):
        user_input = input(
            "===== Welcome to Chatbook =====\n"
            "1. Signup\n"
            "2. Signin\n"
            "3. Write a Post\n"
            "4. Message a friend\n"
            "5. Exit\n"
            "Select option: "
        )

        print()

        if user_input == "1":
            self.signup()

        elif user_input == "2":
            self.signin()

        elif user_input == "3":
            self.writePost()

        elif user_input == "4":
            self.messageFriend()

        else:
            exit()

    def signup(self):
        if self.username is not None:
            print("Account already exists. Please sign in.\n")
            self.menu()
            return

        self.username = input("Enter a username: ")
        self.password = input("Enter a password: ")

        print("\nSignup successful! Please sign in.\n")
        self.menu()

    def signin(self):
        if self.username is None:
            print("No account found. Please sign up first.\n")
            self.menu()
            return

        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == self.username and password == self.password:
            self.loggedIn = True
            print("\nSignin successful! Welcome to Chatbook.\n")
        else:
            print("\nInvalid credentials. Please try again.\n")

        self.menu()
    def writePost(self):
        if not self.loggedIn:
            print("Please sign in to write a post.\n")
            self.menu()
            return

        post_content = input("Write your post: ")
        print(f"\nPost submitted: {post_content}\n")
        self.menu()
    def messageFriend(self):
        if not self.loggedIn:
            print("Please sign in to message a friend.\n")
            self.menu()
            return

        friend_username = input("Enter your friend's username: ")
        message_content = input("Write your message: ")
        print(f"\nMessage sent to {friend_username}: {message_content}\n")
        self.menu()