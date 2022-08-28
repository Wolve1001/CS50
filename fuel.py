while True:
    try:
        a=input("Fraction: ")
        n,d=a.split("/")
        m=int(n)
        o=int(d)
        if m<=o:
            p=(m/o)*100
            q=round(p)
        else:
            continue
    except (ValueError,ZeroDivisionError) as e:
        pass
    else:
        if p<=1:
            print("E")
        elif p>=99:
            print("F")
        else:
            print(f"{q}%")
        break
