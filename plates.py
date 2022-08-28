def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s[len(s)-1].isdigit():
        if 2<len(s)<6:
           for i in s:
               if i.isalnum():
                  if s[0].isalpha() and s[1].isalpha():
                        if i=="0":
                            if s[i-1].isdigit() and s[i-1]!="0":
                                return True
                            else:
                                return False
                        else:
                            return True
                  else:
                    return False
               else:
                return False
        else:
            return False
    else:
        return False


main()
