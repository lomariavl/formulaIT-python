def find_common_participants(group_first: str, group_second: str, separator=','):
    return sorted(list(set(group_first.split(separator)) & set(group_second.split(separator))))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
participants = find_common_participants(participants_first_group, participants_second_group, '|')
print(participants)
