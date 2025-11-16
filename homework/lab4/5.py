# Задача 5: Проверка на анаграмму
#
# Условие: Даны две строки. Необходимо определить,
# являются ли они анаграммами (содержат
# одинаковые символы с одинаковой частотой).
# 
# string1 = "listen"
# string2 = "silent"
# Вывод: True

string1 = "listen"
string2 = "silent"

if sorted(string1) == sorted(string2):
    print("True")
else:
    print("False!")
