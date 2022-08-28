mon=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        da=input("Date: ").strip()
        a=0
        if da[0].isnumeric():
           m,d,y=da.split("/")
           d1=int(d)
           m1=int(m)
           if d1>31 or m1>12:
            continue
           print(f"{y}-{m1:02}-{d1:02}")
        elif da[0].isalpha():
           m,d,y=da.split()
           if len(d)==2:
              d=d[0]
           elif len(d)==3:
              d=d[0]+d[1]
           else:
            continue
           d1=int(d)
           if d1<=31:
            if m in mon:
              m1=int(mon.index(m)+1)
              print(f"{y}-{m1:02}-{d1:02}")
           else:
            continue
    except ValueError:
        pass
    else:
        break
