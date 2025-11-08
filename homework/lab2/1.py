def function(x):
    if -2 <= x < 2:
        return x * x
    elif x >= 2:
        return x ** 2 + 4 * x + 5
    elif x < -2:
        print("возвращаем 4") #возвращаемое число не является результатом вычисления
        return 4
    
x = int(input("Введите любое целое число (положительное или отрицательное): "))
print(function(x))
