# Задача 2: Подсчёт частоты элементов
#
# Условие: Дана строка, состоящая из символов.
# Необходимо подсчитать частоту каждого символа в
# строке и вывести её.
#
# string = "abracadabra"
# Вывод: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

string = "abracadabra"

char_frequency = {}

for char in string:
    char_frequency[char] = char_frequency.get(char, 0) + 1

print(char_frequency)
