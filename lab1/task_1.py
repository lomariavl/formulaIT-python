numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_none = numbers.index(None)
average_value = sum((num for num in numbers if num)) / len(numbers)
numbers[index_none] = average_value

print("Измененный список:", numbers)