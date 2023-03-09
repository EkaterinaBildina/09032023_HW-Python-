# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
inputnumber = int(input("Введите трехзначне число:  "))

if (inputnumber <= 999 and inputnumber >= 100):
    num1 = int(inputnumber % 10)
    num2 = int(inputnumber/10 % 10)
    num3 = int(inputnumber/100 % 10)
    print(f"{num1 + num2 + num3}")
else:
    print("Ошибка ввода числа!")
