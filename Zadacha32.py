# Задача 32: 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def indexes_of_values_in_range(our_list):
    our_range_min = int(input("Введите минимальное значение диапазона: "))
    our_range_max = int(input("Введите максимальное значение диапазона: "))
    if our_range_min > our_range_max:
        raise ValueError("Минимум не может превышать максимум!")
    indexes = []
    for i in range(0, len(our_list)):
        if our_range_min <= our_list[i] <= our_range_max: # Синтаксис пайтона позволяет так написать.
            indexes.append(i)
    if len(indexes) == 0:
        print("Значения всех элементов массива не попадают в указанный диапазон.")
    else:
        print(indexes)


our_list = list(map(int, input("Введите числа через пробел: ").split()))
indexes_of_values_in_range(our_list) 