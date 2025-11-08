while True:
    user_input_A = input("Введите целое натуральное число А до 100: ")
    if user_input_A.isdigit() and int(user_input_A) > 0 and int(user_input_A) <= 100:
        a = int(user_input_A)
        break
    else:
        print("Введено некорректное значение. Попробуйте снова.")

while True:
    user_input_B = input("Введите целое натуральное число B до 100: ")
    if user_input_B.isdigit() and int(user_input_B) > 0 and int(user_input_B) <= 100 and int(user_input_B) >= int(user_input_A):
        b = int(user_input_B)
        break
    else:
        print("Введено некорректное значение. Попробуйте снова.")

x = 0 

for i in range(a, b + 1):
    x = x + i ** 2

print(f"Сумма квадратов всех чисел от {a} до {b} равна {x}")
