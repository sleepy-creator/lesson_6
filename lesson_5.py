# Урок №5
X = int(input("Напишите любое число от 1 до 1000: "))
# Проверка на правильность ввода числа
if X >= 1001:
    print("Ошибка, вы ввели число больше чем 1000")
    print("Повторите попытку.")
    quit()

if X <= 0:
    print("Ошибка, вы ввели число меньше 1")
    print("Повторите попытку.")
    quit()
# Делаем это число простым
def func():

    if X / X == 1 or X:
        pass
    else: X + 1
    return X

print("Теперь это число простое!")
# Выводим список делителей числа
def f(num):
    list = []
    step = 2
    while step * step <= num:
        if num % step == 0:
            num //= step
            list.append(step)
        else:
            step += 1
    if num > 1:
        list .append(num)
    return list
print ("Список делителей числа: ",f(X))
# Выводим самый большой делитель
def max(number):
    number_list = f(number)
    max_num = 0
    for index in number_list:
        if index > max_num:
            max_num = index
    return (max_num)
print("Самый большой делитель: ",max(X))