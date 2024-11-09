# Создаем список с числами
numbers = [1, 2, 3, 4, 5]

# Создаем пустой список для хранения квадратов
squares = []

# Проходим по каждому числу в списке и находим его квадрат
for number in numbers:
    square = number ** 2
    squares.append(square)  # Добавляем квадрат в новый список

# Выводим оригинальный список и список квадратов
print("Оригинальные числа:", numbers)
print("Квадраты чисел:", squares)
