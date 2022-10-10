# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

# Methods

def create_polynome(num):
    polynome_list = []
        
    for i in range (1, num+1):
        coefficient = random.randint(0, 100)
        element = f"{coefficient}x^{i}"
        if element[-1] == "1":
            element = element[:-2]
        if coefficient != 0:
            polynome_list.append(element)
        
    polynome_list.reverse()
    free_element = f"{random.randint(1, 100)}"
    polynome_list.append(free_element)
    return polynome_list


# Code

k = int(input("Введите коэффициент степени многочлена в виде целого числа от 0 до 100: "))
my_separator = " + "
my_polynome = my_separator.join(create_polynome(k))

print(f"{my_polynome} = 0")

with open("polynome.txt", "w") as data:
    data.writelines(my_polynome + " = 0")
