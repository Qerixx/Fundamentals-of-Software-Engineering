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

def analyze_workout_types(workouts):
    count_run = 0
    avg_time_run = []
    avg_calories_run = []

    count_strength = 0
    avg_time_strength = []
    avg_calories_strength = []

    count_bike = 0
    avg_time_bike = []
    avg_calories_bike = []

    count_swim = 0
    avg_time_swim = []
    avg_calories_swim = []

    count_walk = 0
    avg_time_walk = []
    avg_calories_walk = []

    for workout in workouts:
        if workout['type'] == 'бег':
            count_run +=1
            avg_time_run.append(workout['duration'])
            avg_calories_run.append(workout['calories'])

        if workout['type'] == 'силовая тренировка':
            count_strength +=1
            avg_time_strength.append(workout['duration'])
            avg_calories_strength.append(workout['calories'])

        if workout['type'] == 'велосипед':
            count_bike +=1
            avg_time_bike.append(workout['duration'])
            avg_calories_bike.append(workout['calories'])

        if workout['type'] == 'плавание':
            count_swim +=1
            avg_time_swim.append(workout['duration'])
            avg_calories_swim.append(workout['calories'])

        if workout['type'] == 'ходьба':
            count_walk +=1
            avg_time_walk.append(workout['duration'])
            avg_calories_walk.append(workout['calories'])

    print('РАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:')
    print(f'Бег: {count_run} тренировок ({(count_run/len(workouts)*100):.1f}%)')
    print(f'  Средняя длительность: {sum(avg_time_run)//len(avg_time_run)} мин')
    print(f'  Средние калории: {sum(avg_calories_run)//len(avg_calories_run)} калорий')

    print(f'Силовая тренировка: {count_strength} тренировок ({(count_strength / len(workouts) * 100):.1f}%)')
    print(f'  Средняя длительность: {sum(avg_time_strength) // len(avg_time_strength)} мин')
    print(f'  Средние калории: {sum(avg_calories_strength) // len(avg_calories_strength)} калорий')

    print(f'Велосипед: {count_bike} тренировок ({(count_bike / len(workouts) * 100):.1f}%)')
    print(f'  Средняя длительность: {sum(avg_time_bike) // len(avg_time_bike)} мин')
    print(f'  Средние калории: {sum(avg_calories_bike) // len(avg_calories_bike)} калорий')

    print(f'Плавание: {count_swim} тренировок ({(count_swim / len(workouts) * 100):.1f}%)')
    print(f'  Средняя длительность: {sum(avg_time_swim) // len(avg_time_swim)} мин')
    print(f'  Средние калории: {sum(avg_calories_swim) // len(avg_calories_swim)} калорий')

    print(f'Ходьба: {count_walk} тренировок ({(count_walk / len(workouts) * 100):.1f}%)')
    print(f'  Средняя длительность: {sum(avg_time_walk) // len(avg_time_walk)} мин')
    print(f'  Средние калории: {sum(avg_calories_walk) // len(avg_calories_walk)} калорий')

def find_user_workouts(users, user_name):
    workouts = load_workouts_data()
    for user in users:
        if user['name'] == user_name:
            id = user['user_id']
    for workout in workouts:
        if workout['user_id'] == id:
            print(workout)
def analyze_user(workouts,user_name):
    users = load_users_data()
    count_workouts = 0
    count_calories = 0
    count_time = 0
    count_distance = 0
    work_type = []
    for user in users:
        if user['name'] == user_name:
            id = user['user_id']
            age = user['age']
            weight = user['weight']
            lvl = user['fitness_level']
    for workout in workouts:
        if workout['user_id'] == id:
            count_workouts += 1
            count_calories +=  workout['calories']
            count_time += workout['duration']
            count_distance += workout['distance']
            work_type.append(workout['type'])
    count_calories_per_workout = count_calories / count_workouts
    workout_type = {}
    for i in work_type:
        workout_type[i]=workout_type.get(i,0)+1
    fav_type = max(workout_type, key=workout_type.get)
    print(f'ДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: {user_name}')
    print('===========================================')
    print(f'Возраст: {age}, Вес: {weight}')
    print(f'Уровень: {lvl}')
    print(f'Тренировок: {count_workouts}')
    print(f'Сожжено калорий: {count_calories}')
    print(f'Общее время: {(count_time/60):.1f} часов')
    print(f'Пройдено дистанции: {count_distance} км')
    print(f'Средние калории за тренировку: {(count_calories_per_workout):.0f}')
    print(f'Любимый тип тренировки: {fav_type}')

def circle_diagram():
    count_run = 0
    count_strength = 0
    count_bike = 0
    count_swim = 0
    count_walk = 0
    workouts = load_workouts_data()
    for workout in workouts:
        if workout['type'] == 'бег':
            count_run += 1

        if workout['type'] == 'силовая тренировка':
            count_strength += 1

        if workout['type'] == 'велосипед':
            count_bike += 1

        if workout['type'] == 'плавание':
            count_swim += 1

        if workout['type'] == 'ходьба':
            count_walk += 1

    y = np.array([(count_run/len(workouts)*100), (count_strength / len(workouts) * 100), (count_bike / len(workouts) * 100), (count_swim / len(workouts) * 100),(count_walk / len(workouts) * 100) ])
    mylabels = ["Бег", "Силовая тренировка", "Велосипед", "Плавание","Ходьба"]
    plt.title('Распределение типов тренировок')
    plt.pie(y, labels=mylabels, startangle=90,autopct='%1.1f%%')
    plt.show()

def pillar_users_diagram():
    stat = []
    users_data = load_users_data()
    workouts = load_workouts_data()
    for user in users_data:
        user_id = user['user_id']
        part = [user_id, 0,4]
        for workout in workouts:
            if user_id == workout['user_id']:
                part[1] += 1  # колво тренировок
                part[2] = user['name'] #имя
        stat.append(part)
    users = []
    for user in stat:
        part = [user[0], user[1],user[2]]
        users.append(part)
    users.sort(key=lambda x: x[1],reverse=True)
    users_names = [0,0,0,0,0,0,0,0,0,0]
    users_workouts = [0,0,0,0,0,0,0,0,0,0]
    i=0
    for user in users:
        users_names[i] = user[2]
        i+=1
    i=0
    for workout in users:
        users_workouts[i] = workout[1]
        i+=1
    plt.bar(users_names, users_workouts, align='center',color='pink')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Пользователи')
    plt.ylabel('Количество тренировок')
    plt.title('Активность пользвателей(Количество тренировок)')
    plt.show()





