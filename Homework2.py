print("Домашнее задание 2")
num = input("Введите число ")
num = float(num)
num = num % 10
if num == 1:
    print("Кот")
elif 2 <= num < 5:
    print("Кота")
else:
    print("Котов")