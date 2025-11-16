# Этот способ не подходит
# Надо всё переделать










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
k = 3

#nested_list = []
#for i in range(0, len(arr), k):
#  nested_list.append(arr[i:i+1])
#print(nested_list)


#for i in range(len(arr) // k):
#    x = []
#    for j in range(k):
#        x.append(arr[i * k + j])
#    newArr.append(x)

#print(newArr)


#current_sum = sum(arr[:k])
#max_sum = current_sum

#for i in range(k, len(arr)):
#    current_sum = current_sum - arr[i-k] + arr[i]
#    if max_sum < current_sum:
#        max_sum = current_sum


#print(max_sum)


