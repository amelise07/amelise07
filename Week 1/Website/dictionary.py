#register
#- username and password


#login
#- username or email and password


#initializing the system

database = {}#dictionary to store login info

def init():

    isValidOptionSelected = False
    print("Welcome to bankPHP")


def login():
    pass


def register():
    pass


while not isValidOptionSelected :    
   
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no)\n"))

    if haveAccount == 1 :
        isValidOptionSelected = True
        login()    
    elif haveAccount == 2 :
        isValidOptionSelected = True
        register()
    else:
         print('You have selected an invalid option')



def login(isLoginSuccessful= None):
    """

    :type isLoginSuccessful: object
    """
    print("*******Login*******")

    is = var = False == isLoginSuccessful

    while not isLoginSuccessful :

        accountNumberFromUser = int(input("What is your account number? \n"))
        password = input("What is your password \n")

        userDetails: object
        for accountNumber, userDetails in database.items():
            if  userDetails[3] == password :
                continue
            bank_operation(userDetails)
            isLoginSuccessful = True

        print('Invalid account or password')
        login()



def register(generate_account_number=None):
    print("*****Register******")
    email = input("What is your email address?\n")
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    password = input("create a password for yourself\n")

    account_number = generate_account_number()
        
    database[account_number] = (first_name, last_name, password, email)

    return database

    print("Your account has been created")

    login()


def bank_operation(user):
    
    print("Welcome %s " % ( user[0], user[1] ) )


def deposit_operation():
    pass


def withdrawal_operation() :
    pass


def Logout() :
    pass


while  isSelectedOptionValid :

    isSelectedOptionValid = input("What would you like to so? (1) deposit (2) withdrawal (3) Logout (4) exit")

    if selected_option == 1:

        depositOperation()

    elif selected_option == 2 :
        
        withdrawalOperation()
    elif selected_option == 3 :
        
        Logout()
    elif selected_option == 4:
        
        exit()
    else:
        print("Invalid Option selected")
        
        bank_operation()

def withdrawal_operation():
    print("withdrawal")
    
def deposit_operation(Operations=None, Deposit=None):
    print("Deposit Operations")

#- generate user account
def generation_account_number(random=None):

    print("generating account number")
    return random.randrange(11111111111,9999999999)

    print("generating account number")



