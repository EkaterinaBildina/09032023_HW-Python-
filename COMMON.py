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


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1 / 24 -> 4  16  4  /  60 -> 10  40  10

paperCraneNum = int(input("Введите число журавликов: "))
numPetr = int(paperCraneNum/6)
numKate = int(2*paperCraneNum/3)
numSergey = numPetr

print("CraneQuantity : Petr Kate Sergey")
print(f"      {paperCraneNum} ->      {numPetr}   {numKate}   {numSergey}")


# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#  *Пример:* 385916 -> yes / 123456 -> no
number = input("Введите номер билета:  ")

if len(number) == 6:
    sum1 = int(number) % 10 + int(int(number)/10) % 10 + int(int(number)/100) % 10
    sum2 = int(int(number)/1000) % 10 + int(int(number)/10000) % 10 + int(int(number)/100000) % 10
    print(f"{number} -> {sum1 == sum2}")
else:
    print("Ошибка ввода числа")


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:* 3 2 4 -> yes // 3 2 1 -> no

numN = int(input("Размер шоколадки n долек:  "))
numM = int(input("Размер шоколадки m долек:  "))
numK = int(input("Отломить количество долек k:  "))

if (numN * numM - numK) % numN == 0 or (numN * numM - numK) % numM == 0:
    print("yes")
else:
    print("no")