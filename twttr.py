def main():
    inpt=input("Input: ")
    print("Output: ",end="")
    for i in inpt:
        if isVowel(i):
            continue
        print(i,end="")
    print("")
def isVowel(b):
    match b:
        case "a"|"e"|"i"|"o"|"u":
            return True
        case "A"|"E"|"I"|"O"|"U":
            return True
        case _:
            return False
if __name__=="__main__":
    main()
