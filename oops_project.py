class Chatbook:
    def __init__(self):
        self.username =""
        self.password = ""
        self.LoggedIn = False
        self.Menu()

    def Menu(self):
        user_input = input("""Welcome to Chatbook! Please choose an option:\n1. SignUp\n2. SignIn\n3. Post\n4. Message a friend \n5. Exit\n""")

        if user_input == "1":
            self.SignUp()
        elif user_input == "2":
            self.SignIn()
        elif user_input == "3":
            self.Post()
        elif user_input == "4":
            self.Message()
        elif user_input == "5":
            print("Thank you for using Chatbook!")
            exit()
        else:
            print("Invalid input. Please try again.")
            self.Menu()


    def SignUp(self):
        user = input("Please enter your username: ")
        pwd = input("Please enter your password: ")
        self.username = user
        self.password = pwd
        print("Account created successfully!")
        self.Menu()

    def SignIn(self):
        if self.username == "" or self.password == "":
            print("Please create an account first.")
            self.Menu()
        else:
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            if username == self.username and password == self.password:
                print("Login successful!")
                self.LoggedIn = True
                self.Menu()
            else:
                print("Invalid credentials. Please try again.")
                self.SignIn()

    def Post(self):
        if self.LoggedIn:
            post_content = input("Please enter your post content: ")
            print(f"Post created: {post_content}")
            self.Menu()
        else:
            print("You need to be logged in to create a post.")
            self.Menu()
    
    def Message(self):
        if self.LoggedIn:
            message_content = input("Please enter your message: ")
            print(f"Message sent: {message_content}")
            self.Menu()
        else:
            print("You need to be logged in to send a message.")
            self.Menu()
    
Kunal = Chatbook()
