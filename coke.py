amount=50
print("Amount Due:",amount)
for i in range(amount):
    coin=int(input("Insert Coin: "))
    if coin in [5,10,25]:
            amount-=coin
            if amount>0:
                print("Amount Due:",amount)
            else:
                print("Change Owed:",abs(amount))
                break
    else:
        print("Amount Due:",amount)
