packets = input()
max_lost_streak = 0
current_streak = 0

if not all(char in '01' for char in packets):
 print("Incorrect input. Use only the symbols '0' and '1'!")

elif len(packets) < 5:
    print('The length of the sequence must be at least 5')

else:
    for i in packets:
        if i == '0':
            current_streak += 1
            max_lost_streak = max(max_lost_streak, current_streak)
        else:
            current_streak = 0
loss = (packets.count('0') / len(packets)) * 100

if loss <=1:
    quality = 'Excellent quality'
elif loss <= 5:
    quality = 'Good quality'
elif loss <= 10:
    quality = 'Satisfactory quality'
elif loss <= 20:
    quality = 'Bad quality'
else:
    quality = 'Critical network status'
print('Total number of packages:', len(packets))
print('Number of lost packets:', packets.count('0'))
print('The length of the longest sequence of lost packets:', max_lost_streak)
print(f'Percentage of losses: {loss}%')
print('Communication quality:', quality)
    


