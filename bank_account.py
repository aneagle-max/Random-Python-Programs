# Version 5
# Any number of accounts - with  list of dictionaries


accounts_list = [] # 1
def new_account(a_name, a_balance, a_password):
    global accounts_list
    new_account_dict = {'name': a_name, 'balance': a_balance, 'password': a_password} 
    accounts_list.append(new_account_dict)  # 2

def show(account_num):
    global accounts_list
    print('Account', account_num)
    this_account_dict = accounts_list[account_num]
    print('          Name', this_account_dict['name'])
    print('          Balance:', this_account_dict['balance'])
    print('          Password:', this_account_dict['password'])
    print()

def get_balance(account_num, password):
    global accounts_list
    this_account_dict = accounts_list[account_num]  # 3 
    if password != this_account_dict['password']:
        print('Incorrect password')
        return None
    return this_account_dict['balance']

def deposit(account_num, amount_to_deposit, password):
    global accounts_list
    this_account_dict = accounts_list[account_num]
    if amount_to_deposit < 0:
        print('You cannot deposit a negative amount')
        return None
    if password != this_account_dict['password']:
        print('Incorrect password')
        return None
    this_account_dict['balance'] += amount_to_deposit
    return this_account_dict

def withdraw(account_num, amount_to_withdraw, password):
    global accounts_list
    this_account_dict = accounts_list[account_num]
    if amount_to_withdraw < 0:
        print('You cannot deposit a negative amount! Enter an amount greater than Zero')
        return None
    if password != this_account_dict['password']:
        print('Incorrect password')
        return None
    if amount_to_withdraw > this_account_dict['balance']:
        print('Insuficient funds!')
        return None
    this_account_dict['balance'] -= amount_to_withdraw
    return this_account_dict
# Create two sample accounts

print("Silver's account is account number:", len(accounts_list))
new_account("Silver", 15764, 'pixie')

print("Maxwell's account is account number:", len(accounts_list))
new_account("Maxwell", 42331, 'maxi')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press n to create a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()

    action = input('WHat do you to do? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get balance')
        user_account_number = int(input('Enter your account number: '))
        user_password = input('Please enter your password: ')
        the_balance = get_balance(user_account_number, user_password)
        if the_balance is not None:
            print('Your balance is:', the_balance)

    elif action == 'd':
        print('Deposit')
        user_account_number = int(input('Enter your account number: '))
        user_amount_deposit = int(input('How much do you want to deposit?: '))
        user_password = input('Please enter your password: ')
        new_balance = deposit(user_account_number, user_amount_deposit, user_password)
        if new_balance is not None:
            print('Your balance is:', new_balance)

    elif action == 'n':
        print('New account')
        user_name = input('What is your name?: ')
        user_starting_amount = int(input('How much are you depositing for a start?: '))
        user_password = input('Enter a password: ')
        user_account_number = len(accounts_list)
        new_account(user_name, user_starting_amount, user_password)
        print('Your new account number is:', user_account_number) 

    elif action == 's':
        print('Show:')
        n_accounts = len(accounts_list)
        for account_number in range(0, n_accounts):
            show(account_number)  

    elif action == 'q':
        break                 


    elif action == 'w':
        print('Withdrawal')
        user_account_number = int(input('Enter your account number: '))
        user_amount_to_withdraw = int(input('Enter amount to withdraw: '))
        user_password = input('Please enter your password: ')
        new_balance = withdraw(user_account_number, user_amount_to_withdraw, user_password)
        if new_balance is not None:
            print('Your balance is:', new_balance) 

print('Done!')     