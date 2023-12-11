users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

num_visits = {'Общее количество': 0, 'Уникальные посещения': 0}
num_visits['Общее количество'] = len(users)
num_visits['Уникальные посещения'] = len(set(users))

print(num_visits)
