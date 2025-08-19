# объявление функции
def merge(list1, list2):
    list1.extend(list2)
    n = len(list1)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list1[j] > list1[j + 1]:                  # если порядок элементов пары неправильный
                list1[j], list1[j + 1] = list1[j + 1], list1[j]  # меняем элементы пары местами 
    return list1

# считываем данные
print('Программа слияния двух списков и их сортировки с использованием функции')
print('Введите числа для первого списка больше 2 чисел и с пробелами:')
numbers1 = [int(c) for c in input().split()]
print('Введите числа для второго списка больше 2 чисел и с пробелами:')
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))