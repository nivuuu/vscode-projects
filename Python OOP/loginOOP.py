class login:
    def __init__(self):
        self.credintials = {}
    def register(self, username, password):
        self.credintials[username] = password


# Checks what the user inputs and decides whether it is valid or not.
    def check(self, user, pas):
        print(self.credintials )
        if user in self.credintials.keys() and pas == self.credintials[user] :
            print("Login successful!")
        else:
            print('Error123: Wrong Username/Password - Please try again')

account = login()
# Ensures the program remains running
Close = False

# Setter
while Close == False:
    print("===============================================")
    print("|              WELCOME TO QA.NET!             |")
    print("===============================================")
    tasks = (input('What would you like to do? Please enter one of the following: [Register], [Login], or [Quit]'))
    # Calling functions
    if tasks == 'Register' or "register":
        Name = (input('Please set a username: '))
        Pword= (input('Please set a password: '))
        account.register(Name, Pword)

# Getter
    if tasks == 'Login' or "login":
        print("Welcome back, please login: ")
        print("===========================")
        loginUsername = (input('Please enter Username: '))
        loginPassword = (input('Please enter Password: '))
        account.check(loginUsername,loginPassword)
    if tasks == 'Quit' or "quit":
        # When all the tasks are complete, close the program.
        print("See you later!")
        Close = True