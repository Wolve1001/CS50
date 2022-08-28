def main():
    t=input("What time is it? ").strip()
    i=float(convert(t))
    if 7.0 <= i <= 8.0:
        print("breakfast time")
    elif 12.0 <= i <= 13.0:
        print("lunch time")
    elif 18.0 <= i <= 19.0:
        print("dinner time")
    else:
        pass

def convert(time):
    x,y=time.split(":")
    a=float(x)
    b=float(y)
    h=round(a,1)
    m=b/60
    ti=round(h+m,1)
    return ti

if __name__=="__main__":
    main()
