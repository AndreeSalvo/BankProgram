# Python Banking Program

def show_balance(balance):
    print('*******************')
    print(f'Your balance is ${balance:.2f}')
    print('*******************')

def deposit():
    print('*******************')
    amount = float(input('Enter an amount to deposit: '))
    print('*******************')

    if amount < 0:
        print('*******************')
        print('That is not a valid amount')
        print('*******************')
        return 0
    else:
        return amount

def withdraw(balance):
    print('*******************')
    amount = float(input('Enter an amount to withdraw: '))
    print('*******************')

    if amount > balance:
        print('*******************')
        print('Insufficient funds')
        print('*******************')
        return 0
    elif amount < 0:
        print("Amount must be greater than 0 ")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print('*******************')
        print('  Banking Program  ')
        print('  AndreeCreditUnionBank  ')
        print('*******************')
        print('1.See Balance')
        print('2.Deposit Money')
        print('3.Withdraw Money')
        print('4.Exit')
        print('*******************')
        choice = input('Enter a choice (1-4): ')

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print('*******************')
            print('That is not a valid choice')
            print('*******************')

    print('*******************')
    print('Thank you! Please come again!')
    print('*******************')
if __name__ == '__main__':
    main()