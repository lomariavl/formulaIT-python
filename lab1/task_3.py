list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

count_players = len(list_players)
team_1 = list_players[:count_players // 2]
team_2 = list_players[count_players // 2:]

print(team_1)
print(team_2)
