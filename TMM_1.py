"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа.
n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
"""
n = int(input('Введите колличество элементов первого множества'))
m = int(input('Введите колличество элементов второго множества'))
print(f'Введите {n} элементов первого множества')
a_list = [int(input()) for _ in range(n)]
print(f'Введите {m} элементов второго множества')
b_list = [int(input()) for _ in range(m)]
a_set = set(a_list)
b_set = set(b_list)
f_set = a_set.intersection(b_set)
if len(f_set) == 0:
    print('Числа не повторяются')
else:
    print(sorted(f_set))