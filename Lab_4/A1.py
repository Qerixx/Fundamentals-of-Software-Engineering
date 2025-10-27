import random
import time

N = int(input('Введите количество примеров: '))
num_answer = 0
total_time = 0

for i in range(N):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    print(f"Вопрос {i+1}/{N}")
    start_time = time.time()
    while True: 
        try:
            answer = int(input(f"{a} × {b} = ")) 
            break 
        except ValueError: 
            print("Пожалуйста, введите целое число!")
    time_spend = time.time() - start_time
    if answer == a * b:
        print('Верно!')
        num_answer += 1
    else:
        print('Неверно!')
    print(f'Время: {(time_spend):.2f}')
    total_time =time_spend + total_time

print('===============')
print('СТАТИСТИКА')
print('===============')
print(f'Общее время: {total_time:.2f}')
print(f'Среднее время на вопрос: {(total_time / N):.2f}')
print(f'Правильных ответов: {num_answer}/{N}')
print(f'Процент правильных ответов: {((num_answer/N)*100):.2f}%')

