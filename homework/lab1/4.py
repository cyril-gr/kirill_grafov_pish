# Задание 4
# Ввести целое число и определить, верно ли, что
# все его цифры расположены в порядке
# возрастания.
#
# Наверное предполагается len(), но сделал так

def function(number_str):
    sorted_digits = "".join(sorted(number_str))
    return number_str == sorted_digits

user_input = input("Введите целое положительное число: ")
if user_input.isdigit() and int(user_input) > 0:
    if function(user_input):
        print("Цифры введенного числа расположены в порядке возрастания!")
    else:
        print("Цифры введенного числа расположены НЕ в порядке возрастания!")
