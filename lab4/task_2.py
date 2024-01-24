import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

indent = 4


def task() -> None:
    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(rows, file, indent=indent)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
