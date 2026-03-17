#Largest differnce(stock logic)
prices=[7,1,5,3,6,4]
min_price=prices[0]
max_profit=0
currennt_profit=0

for i in range(len(prices)):
    #print(prices[i])
    if prices[i]<min_price:
        min_price=prices[i]
        print(f"min price is {min_price}")
        currennt_profit=prices[i]-min_price
        print(f"current profit is {currennt_profit}")
        if currennt_profit>max_profit:
            max_profit=currennt_profit
            print(f"max profit is {max_profit}")
print(f"max profit is {max_profit}")            
