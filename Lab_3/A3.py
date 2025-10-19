prev = int(input(''))
now = int(input(''))

if prev<now:
    used = now - prev
else:
    used = 10000 - prev + now

if used<=300:
    pay = 21

elif used>300 and used<=600:
    pay = 21 + (used-300)*0.06

elif used>600 and used<=800:
    pay = 21 + 300*0.06 + (used - 600)*0.04

elif used>800:
    pay = 21 + 300*0.06 + 200*0.04 + (used - 800)*0.025

cost = used/pay

print(f"{prev:<12} {now:<8} {used:<12} {payment:<10.2f} {price:<12.2f}")