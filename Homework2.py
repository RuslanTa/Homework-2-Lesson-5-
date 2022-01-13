print("Домашнее задание 2")
num = input("Введите число в интервале 1 - 2000: ")
num = float(num)
new_num = num % 10
if (num < 1) or (num > 2000):
    print("Число не входит в заданный интервал")
else:
    if new_num == 1:
        print("Кот")
    elif 2 <= new_num < 5:
        print("Кота")
    else:
        print("Котов")