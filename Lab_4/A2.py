n = int(input('Enter n: '))
m = int(input('Enter m: '))

print(f'Rectangle {n}*{m}:')
for i in range(n):
    for j in range(m):
        print('#', end='')
    print()

print(f'The right triangle {n}*{m}:')

for i in range(1, n + 1):
    for j in range(i):
        print('#', end='')
    print()

print(f'Frame {n}*{m}:')
for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            print('#', end='')
        else:
            print(' ', end='')
    print()