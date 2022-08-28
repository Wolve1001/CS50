i=input('Expression:').strip()
x,y,z=i.split()
j=int(x)
k=int(z)
match y:
    case "+":
        m=float(j+k)
        print(f'{m:.1f}')
    case "-":
        m=float(j-k)
        print(f'{m:.1f}')
    case "*":
        m=float(j*k)
        print(f'{m:.1f}')
    case "/":
        m=float(j/k)
        print(f'{m:.1f}')
