# Лаба1, зад.1
while True:
    user_input = input("Введите целое натуральное число до 100: ")
    if user_input.isdigit() and int(user_input) > 0 and int(user_input) <= 100:
        number = int(user_input)
        for i in range(1, number + 1):
            print(f"Квадрат числа {i} равен: {i ** 2}")
            print(f"Куб числа {i} равен: {i ** 3}")
        break
    else:
        print("Введено некорректное значение. Попробуйте снова.")
