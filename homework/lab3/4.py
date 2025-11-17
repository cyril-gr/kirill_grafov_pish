# 4. Поиск максимальной суммы
# подмассива фиксированной длины
#
# Дан список целых чисел и длина подмассива k.
# Нужно найти подмассив длины k, сумма
# элементов которого будет максимальной.
#
# Вход: array = [1, -2, 3, 4, -1, 2, 1, -5, 4]
# k = 3
# Выход: [3, 4, -1] (Сумма 6)

arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
newArr = []
nestedList = []
k = 3

x = len(arr)

for i in range (0, len(arr)):
    if x < 3:
        break
    else:
        newArr += (arr[i], arr[i + 1], arr[i + 2])
        x -= 1

#print(newArr)

for j in range(0, len(newArr), k):
    nestedList.append(newArr[j:j+k])

#print(nestedList)

max_list = max(nestedList, key = sum)
max_sum = sum(max(nestedList, key=sum))

print(arr)
print("Подмассив ", max_list, "Сумма ", max_sum)
