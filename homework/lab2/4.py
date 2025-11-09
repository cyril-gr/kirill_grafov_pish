# Задание 4
# Составить функцию, которая определяет сумму
# цифр в числе

def digitsSum(x):
    sumOfDigits = 0    
    while x > 0:
        digit = x % 10
        sumOfDigits = sumOfDigits + digit
        x = x // 10
    return sumOfDigits

x = int(input("Введите любое число не менее 10: "))
print(f"Сумма цифр введенного числа: {digitsSum(x)}")
