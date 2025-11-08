def strDigitsComparison(number_str):
    sorted_digits = "".join(sorted(number_str))
    return number_str == sorted_digits

while True:
    user_input = input("Введите целое положительное число: ")
    if user_input.isdigit() and int(user_input) > 0:
        if strDigitsComparison(user_input):
            print("Цифры введенного числа расположены в порядке возрастания!")
        else:
            print("Цифры введенного числа расположены НЕ в порядке возрастания!")
