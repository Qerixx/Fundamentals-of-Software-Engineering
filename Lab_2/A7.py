x1 = int(input('Enter x1'))
y1 = int(input('Enter y1'))
x2 = int(input('Enter x2'))
y2 = int(input('Enter y2'))

color1 = 'White' if (x1 + y1) % 2 == 0 else 'Black'
color2 = 'White' if (x2 + y2) % 2 == 0 else 'Black'

if color1 == color2:
    print("YES")
    print(color1)
else:
    print("NO")