# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arithmetic_progression_as_a_list():
    our_progression = [int(input("Введите первый член прогрессии: "))]
    diff_of_progression = int(input("Введите разность прогрессии: "))
    n = int(input("Введите количество членов прогрессии: "))
    for i in range(1, n):
        n_i = our_progression[0] + i * diff_of_progression
        our_progression.append(n_i)
    return our_progression


print(arithmetic_progression_as_a_list())