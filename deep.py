i=input("What is the answer to the Great Question of Life, the Universe and Everything?").strip().lower()
match i:
    case "42"|"forty-two"|"forty two"|"Forty-two"|"Forty two":
        print("Yes")
    case _:
        print("No")
        
