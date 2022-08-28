from collections import OrderedDict
gro=[]
while True:
    try:
        item=input().upper()
        gro.append(item)
    except EOFError:
        break
res={}
for i in gro:
    res[i]=gro.count(i)
r=OrderedDict(sorted(res.items()))
for i in r:
    print(res[i],i)
