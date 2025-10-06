x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))

if x1>8 or y1>8 or x2>8 or y2>8: print('Incorrect parameter value') 
else:
    if x1<0 or y1<0 or x2<0 or y2<0: print('Incorrect parameter value') 
    else:
        if (x1 + y1) % 2 == 0: 
            color1 = 'White' 
        else: 
            color1 ='Black'

        if (x2 + y2) % 2 == 0: 
            color2 = 'White' 
        else: 
            color2 ='Black'

        if color1 == color2:
            print("YES")
            print(color1)
        else:
            print("NO")
