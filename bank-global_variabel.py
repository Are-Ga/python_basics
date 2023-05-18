# global variabels
balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    # this will not work as the balance is a variable that is not mutable:
    # balance += n

    # to make it mutable we need to add a explanation to python that it needs to use the global balance:
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()
