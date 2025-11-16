# Задача 1: Уникальные элементы
#
# Условие: Дана строка, содержащая несколько слов.
# Найдите все уникальные слова в строке и выведите
# их в алфавитном порядке.
#
# sentence = "apple banana apple orange banana kiwi"
# Вывод: ['apple', 'banana', 'kiwi', 'orange']

sentence = "apple banana apple orange banana kiwi"
words = sentence.split()
result = sorted(list(set(words)))
print(result)
