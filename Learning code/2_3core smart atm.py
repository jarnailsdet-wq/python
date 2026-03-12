# smart atm
account_balance=5000
wid=int(input("How much withdraw : "))
balance=0
if wid>account_balance:
    print("Insuficiant balance")
elif wid<=account_balance:
    balance=account_balance-wid
    print(f"take your cash new balance is : {balance}")
    