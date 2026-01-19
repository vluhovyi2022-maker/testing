def find_min(numbers: list):
    """
    Повертає мінімальне число зі списку
    """
    if not numbers:
        raise ValueError("Список не повинен бути порожнім")

    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num

    return min_value
