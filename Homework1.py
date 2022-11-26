# 1) Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в
# переменные, выведите на экран.

#a = 23
#b = 86
#print(a + b)
#print('Введите a: ')
#a = input()
#print(a)
#print('Введите b: ')
#b = input()
#print(b + a)
#print('Введите n: ')
#n = int(input())
#print('Введите m: ')
#m = int(input())
#print(n + m)

# 2) Пользователь вводит время в секундах. Переведите время в часы, минуты
# и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

print('Введите время(сек.): ')
time = int(input())
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time % 3600 % 60
print(f'Время: {hours}:{minutes}:{seconds}')

# 3) Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

print('Введите число: ')
n = input()
first_number = n
second_number = n + n
third_number = n + n + n
sum = int(first_number) + int(second_number) + int(third_number)
print(f'Искомое число равно: {sum}')

# 4) Пользователь вводит целое положительное число. Найдите самую большую
# цифру в числе. Для решения используйте цикл while и арифметические операции.

print('Введите число: ')
number = int(input())
max_number = number % 10
while number >= 1:
    number = number // 10
    if number % 10 > max_number:
        max_number = number % 10
    elif number > 9:
        pass
print(f'Максимальная цифра числа: {max_number}')



