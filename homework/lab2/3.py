# Задание 3
# Составить логическую функцию, которая
# опеределяет, верно ли, что в заданном числе
# сумма цифр равна произведению
#
# Правильно ли я понял задание? Единственный вариант 22?

def equalOrNot(x):
    sumOfDigits = 0
    prodOfDigits = 1    
    while x > 0:
        digit = x % 10
        sumOfDigits = sumOfDigits + digit
        prodOfDigits = prodOfDigits * digit
        x = x // 10
    return sumOfDigits == prodOfDigits

x = int(input("Введите любое число не менее 10: "))

if equalOrNot(x):
    print("Сумма чисел равна произведению чисел")
else:
    print("Сумма чисел НЕ равна произведению")
