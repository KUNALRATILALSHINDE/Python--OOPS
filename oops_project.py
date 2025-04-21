class Chatbook:
    def __init__(self):
        self.username =""
        self.password = ""
        self.LoggedIn = False
        self.Menu()

    def Menu(self):
        user_input = input("""Welcome to Chatbook! Please choose an option:\n1. SignUp\n2. SignIn\n3. Post\n4.Message a friend \n5. Exit\n""")

        if user_input == "1":
            self.SignUp()
        elif user_input == "2":
            self.SignIn()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
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

Kunal = Chatbook()
