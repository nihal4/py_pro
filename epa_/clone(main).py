ids = [1234, 5678, 9101]  # user ids of bank user
pas = [1245, 3256, 6589]  # pass for bank users
user_balance = [1000, 5000, 6000]  # amount of bak users


def register():  # register is under development
    print("\n under work \n")


def user_inter(index):  # user ui form here
    print("\nWelcome!!\n")
    while True:  # used so that users can select same option more than one time
        cmd = int(input("1.check balance\n2.add money\n3.withdraw\n0.logout\n=>"))
        if cmd == 1:
            print(f"\nbalance: {user_balance[index]}\n")  # showing balance
        elif cmd == 2:
            add = int(input("set an amount: "))
            user_balance[index] = user_balance[index] + add  # calculating user money
            print(f"\nnew balance :{user_balance[index]}")
        elif cmd == 3 and user_balance[index] > 0:
            remove = int(input("set an amount: "))
            if remove > user_balance[index]:  # checking if user ask more than his balance
                print("\nyou don't have that much cash in your account!!\n")
            else:
                user_balance[index] = user_balance[index] - remove  # calculating balance after withdraw
                print(f"\nnew balance :{user_balance[index]}")
        elif cmd == 3 and user_balance[index] == 0:  # stopping user to ask for withdraw when he has no balance left
            print("\nyour balance is empty\n")
        elif cmd == 0:  # logout option
            start()  # calling start function for bank default interface
            break
        else:
            print("\ninvalid option!!!\n")


def login():  # login function start from here
    x = 3  # taking constant x and i
    i = 2
    while x != 0 and i != 0:  # while loop for asking user id
        print("\nLogin\n")
        ask_id = int(input('Id :: '))
        if ask_id in ids:  # checking if input id is in bank server [1234, 5678, 9101]
            for y in range(2):  # loop for user password
                password = int(input('pass :: '))  # asking pass
                if password in pas:  # checking if pass in bank server [1245, 3256, 6589]
                    if pas.index(password) == ids.index(ask_id):  # checking if password index match with users index
                        user_inter(ids.index(ask_id))  # calling bank ui with user array index
                        break  # break for braking this loop
                else:
                    i = i - 1  # calculating chance of entering  password
                    print("\nwrong pin !!\n")

        else:
            x = x - 1
            print("\n try again \n")


def chose(num):  # chose function starts here .It's for making choice
    if num == 1:
        login()  # calling login function from line 36
    elif num == 2:
        register()  # calling register function from line 6
    else:
        print("\ninvalid option\n")


def start():  # function for giving option on bank
    while True:  # used while loop so that users can user this interface more than one time
        choice = input("\nWelcome to Bank\n1.login\n2.register\n=>")  # Asking user to give input
        chose(int(choice))  # calling chose() function form line 58 and giving int value of choice line 69


if __name__ == "__main__":  # code runs from here
    start()
