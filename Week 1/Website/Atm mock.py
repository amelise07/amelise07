name = input("What is your username? \n")
allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']

if(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):

        print('Welcome %s'% name)
        print('these are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')
        import datetime
        now = datetime.datetime.now()
        print ("Current date and time : ")
        print (now.strftime("%Y-%m-%d %H:%M:%S"))


        selectedOption = int(input('Please select an option:'))

        print(selectedOption)

        if(selectedOption == 1):
            print('you selected %s' % selectedOption)
            input('How much cash would you like to withdraw? \n')
            print('Take your cash!')
            
        
        elif(selectedOption == 2):
            print('you selected %s' % selectedOption)
            print('How much would you like to deoposit?')
            input('How much would you like to deposit? \n')
            
        elif(selectedOption == 3):
            print('you selected %s' % selectedOption)
            input('What issue will you like to report? \n')
            print('Thank you for contacting us.')

            
        else:
            print('invalid Option selected, please try again')

    else:
        print('Password Incorrect, please try again')

else:
    print('Name not found please try again')