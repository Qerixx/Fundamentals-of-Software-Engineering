import xml.etree.ElementTree as ET


def  load_users_data():
    try:
        tree_users = ET.parse('users.xml')
        users_data =[]
        for user in tree_users.findall('user'):
            user_data ={
                'user_id': int(user.find('user_id').text),
                'name': (user.find('name').text),
                'age': int(user.find('age').text),
                'weight': int(user.find('weight').text),
                'fitness_level': (user.find('fitness_level').text)}
            users_data.append(user_data)
        return users_data
    except FileNotFoundError:
        print("File not found")
        return []

def  load_workouts_data():
    try:
        tree_workouts = ET.parse('workouts.xml')
        workouts_data =[]
        for workout in tree_workouts.findall('workout'):
            workout_data ={
                'workout_id': int(workout.find('workout_id').text),
                'user_id': int(workout.find('user_id').text),
                'date': (workout.find('date').text),
                'type': (workout.find('type').text),
                'duration': int(workout.find('duration').text),
                'distance': float(workout.find('distance').text),
                'calories': int(workout.find('calories').text),
                'avg_heart_rate': int(workout.find('avg_heart_rate').text),
                'intensity': (workout.find('intensity').text)}
            workouts_data.append(workout_data)
        return workouts_data
    except FileNotFoundError:
        print("File not found")
        return []

def get_stats(user_data,workouts_data):
    count_workouts = 0
    count_users = 0
    count_calories = 0
    count_time = 0
    count_distance = 0
    for workout in workouts_data:
        count_workouts += 1
    for user in user_data:
        count_users += 1
    count_calories = sum(workout['calories'] for workout in workouts_data)
    count_time = sum(workout['duration'] for workout in workouts_data) #в минутах
    count_distance= sum(workout['distance'] for workout in workouts_data)
    count_time = count_time / 60
    print('ОБЩАЯ СТАТИСТИКА\n')
    print('===========================\n')
    print(f'Всего тренировок: {count_workouts}')
    print(f'Всего пользователей: {count_users}')
    print(f'Сожжено калорий: {count_calories}')
    print(f'Общее время: {count_time:.2f} часов')
    print(f'Пройдено дистанции: {count_distance} км')

def analyze_user_activity(users_data):
    stat = []
    workouts = load_workouts_data()
    for user in users_data:
        user_id = user['user_id']
        part = [user_id, 0, 0, 0,0,0]
        for workout in workouts:
            if user_id == workout['user_id']:
                part[1] += 1 #колво тренировок
                part[2] += workout['calories'] #колво калорий
                part[3] += workout['duration'] #время в минутах!!
                part[4] = user['name']
                part[5] = user['fitness_level']
        stat.append(part)
    users = []
    max_users= []
    for user_top in stat:
        part = [user_top[0], user_top[1],user_top[2],user_top[3], user_top[4], user_top[5]]
        users.append(part)
    users.sort(key=lambda x: x[1], reverse=True)
    max_users = [users[0],users[1],users[2]]

    print('ТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:\n')
    num = 1
    for user in max_users:
        print(f'{num}. {user[4]}({user[5]})')
        print(f'Тренировок: {user[1]}')
        print(f'Калорий: {user[2]}')
        print(f'Время: {(user[3]/60):.1f} часов')
        num += 1

        



