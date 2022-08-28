taq={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
c=0
while True:
    try:
        item=input("Item: ").title()
        if item in taq:
            c+=taq[item]
            print(f"Total: ${c:.2f}")
    except EOFError:
        print("")
        break
