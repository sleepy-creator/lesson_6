# Урок №5
X = int(input("Напишите любое число от 1 до 1000: "))


# Проверка на правильность ввода числа
if 0 <= X <= 1000:
    print()
else:
    print("Вы ввели число, которое либо меньше 1, либо больше 1000")
    print('У вас осталась 1 попытка')
    X = int(input())
    if 0 <= X >= 1001:
        quit()

# Делаем это число простым
def func():

    if X / X == 1 or X:
        pass
    else: X + 1
    return X

print("Теперь это число простое!")
# Выводим список делителей числа
step = 2

def f(num):
    list = []
    global step
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
max_num = 0
def max(number):
    number_list = f(number)
    global max_num
    global index
    for index in number_list:

        if index > max_num:
            max_num = index
    return (max_num)
print("Самый большой делитель: ",max(X))

# Test_№1

if 0 < X :
    print("Test_1 Complete!")
else:
    print("Test_1 Failed!")
# Test_№2
if X / X ==  1 or X:
    print("Test_2 Complete!")
else:
    print("Test_2 Failed!")
# Test_№3
if max_num == index:
    print("Test_3 Complete!")
else:
    print("Test_3 Failed!")
# Test_№4
if step == 2:
    print("Test_4 Complete!")
else:
    print("Test_4 Failed!")
# Test_№5
if X < 1001:
    print("Test_5 Complete!")
else:
    print("Test_5 Failed!")




