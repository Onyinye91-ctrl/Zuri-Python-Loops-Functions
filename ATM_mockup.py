import random
import datetime
now = datetime.datetime.now()
date = now.strftime("%x")
time = now.strftime("%I:%M %p") 
date_time = now.strftime ("%Y:%m:%d, %H:%M:%S")

database = {}

def welcome():

   
    print("Welcome to Style Bank Plc. Date of login: %s and Time of login: %s " % (date, time))
    print("\n")
    print("Do you have an account with us")
    print("Press '1' for Yes")
    print("Press '2' for No")
    print("Press '3' for exit")
 
    yourAccount = int(input("Enter Your Answer: "))
   
    if yourAccount == 1:
        login()

    elif yourAccount == 2:
        register()

    elif yourAccount == 3:
        exit()

    else:
        print("You have selected invalid option")
        welcome()


def register():
    print("**********Welcome to Style Bank Plc Registeration Portal**********")
    first_name = input("Enter you first_name: \n")
    last_name = input("Enter you last_name: \n")
    passwordUser = input("Enter you password: \n")
    email = input("Enter You email: \n")


    accountNumber = generate_Account_No()
    balance = 0
    database[accountNumber] = [first_name, last_name, passwordUser, email,balance]
    print("Your Account have been Successfully created")
    print("Your Account No is %d" % accountNumber)
    print("Deposit into your Account to activate it")
    login()

def login():
    print("\n")
    print("**********LOGIN**********")
    user_Account = int(input("Enter Your Account No: "))
    if user_Account in database.keys():
        print("Your Acccount No is recognized")
        print("\n")
        user_password = input("Enter Your Password: ")
        print("\n")
        for user_details in database.values():
            if user_password == user_details[2]:
                print("Password entered Successfully")
                print("Welcome %s %s" %(user_details[0], user_details[1]))
                bankOperation(user_details)
            else:
                print("Incorrect Password...please try again")
                print("Press '1' to try again")
                print("Press '2' to exit")
                response = int(input("Enter Your response: "))
                if response == 1:
                    login()
                else: 
                    exit()
    else:
        print("Incorrect Account No")
        print("Press '1' to try again")
        print("Press '2' to exit")
        response = int(input("Enter Your response: "))
        if response == 1:
            login()
        else: 
            exit()

def logout():
    print("You have logged Out")
    print("\n")
    welcome()

def exit():
    print("Thank You for Banking with us. Do have a nice Day. %s %s." % (date, time))   


def bankOperation(user):
    print("What would you like to do.")
    print("Press '1' to deposit")
    print("Press '2' to withdraw")
    print("Press '3' to complaint")
    print("Press '4' to check balance")
    print("Press '5' to logout")

    selectedOption = int(input("What would you like to do: \n"))
    if selectedOption == 1:
        deposit(user)
    elif selectedOption ==2:
        withdraw(user)
    elif selectedOption ==3:
        customer_care(user)
    elif selectedOption == 4:
        check_balance(user)
    elif selectedOption == 5:
        logout(user)
    else:
        print("Invalid Selection")
        print("\n")
        bankOperation(user)
   
def deposit(user):
    print("\n")
    print("**********DEPOSIT**********")
    amount = int(input("How much would you like to deposit: \n"))
    user[-1] = user[-1] + amount
    print("Your Deposited %d. Your current balance is %d" %(amount, user[-1]))
    print("\n")
    bankOperation(user)

def withdraw(user):
    print("\n")
    print("**********WITHDRAW**********")
    amount = int(input(("How much do you want to Withdraw: \n")))
    if user[-1] == 0:
        print("Your balance is %d. Please make Deposit" % (user[-1]))
    elif user[-1] < amount:
        print("Insufficient Balance, Please make Deposit")
        bankOperation(user)
    else:
        user[-1] = user[-1] - amount
        print(f"Please Take your cash: {amount}")
        print(f"Your Remaining Balance is: {user[-1]}")
        print("\n")
        bankOperation(user)

def customer_care(user):
    print("\n")
    print("**********CUSTOMER CARE CENTER**********")
    complaint = input("What would you like to Report? \n")
    print("Your Complaint have been Recorded. You will be contacted Soon.")
    print("Thank You for Banking with Us.")
    print("\n")
    bankOperation(user)

def check_balance(user):
    print(f"Your Balance is {user[-1]}")
    print(f"Thank you for banking with us {user[0]} {user[1]}")
    print("\n")
    bankOperation(user)


def generate_Account_No():

    return random.randrange(1111111111,9999999999)

def logout(user):
    welcome()

#### Start Application #####

welcome()






