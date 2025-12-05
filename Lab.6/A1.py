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
    return count_workouts, count_users, count_calories, count_time, count_distance
        
