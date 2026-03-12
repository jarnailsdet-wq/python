#dry run for logiic
balance=100
withdrawals=[20,50,40]

for amount in withdrawals:
    print("Current balance "+str(balance))
    #  amount=int(input("Enter you Amount : "))
    print(amount)
    balance=balance-amount
    print(f"balance :{balance}")
    if balance<0:
        print("your balance is going below zero")

