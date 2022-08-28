c=input("camelCase: ")
for i in c:
    if i.isupper():
        print("_",end="")
    print(i.lower(),end="")
print("")
