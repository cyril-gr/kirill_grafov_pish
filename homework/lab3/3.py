# 3. Разворот блоков в списке
#
# Дан список чисел и размер блока. Нужно
# развернуть элементы в каждом блоке по
# отдельности. Если последний блок меньше по
# размеру, его нужно оставить без изменений.
#
# Вход: array = [1, 2, 3, 4, 5, 6, 7]
# block_size = 3 
# Выход: [3, 2, 1, 6, 5, 4, 7]

arr = [1, 2, 3, 4, 5, 6, 7]
blockSize = 3
newArr = []
tail = []

for i in range(len(arr) // blockSize):
    x = []
    for j in range(blockSize):
        x.append(arr[i * blockSize + j])
    newArr.append(x)

for f in range(len(newArr)):
     newArr[f] = list(reversed(newArr[f]))

for h in range(len(arr) % blockSize):
    tail.append(arr[-(h+1)])

tail = list(reversed(tail)) # на случай если список будет изменен, например добавится число 8

newArr.append(tail)
print("Исходный список: ", arr)
print("Новый список: ", newArr)

# Или же, если необходимо вывести простым списком (не вложенным):
flatList = []
for sublist in newArr:
    for item in sublist:
        flatList.append(item)
print("Выход: ", flatList)
