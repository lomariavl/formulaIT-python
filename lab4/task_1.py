import json
INPUT_FILENAME = "input.json"


def task() -> float:
    with open(INPUT_FILENAME) as file:
        data_json = json.load(file)
    result = sum(value['score'] * value['weight'] for value in data_json)
    return round(result, 3)


print(task())
