class Chatbook:
    def __init__(self):
        self.username =""
        self.password = ""
        self.LoggedIn = False
        self.Menu()

    def Menu(self):
        user_input = input("""Welcome to Chatbook! Please choose an option:\n1. SignUp\n2. SignIn\n3. Post\n \4.Message a friend \n5. Exit\n""")

        if user_input == "1":
            pass
        elif user_input == "2":
            pass
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


Kunal = Chatbook()
