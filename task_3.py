# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# Method (метод формирования списка чисел пользователем, определяем пробел в качестве разделителя)

def input_list():   
    list_string = input("Введите некоторое количество элементов (чисел или знаков) через пробел: ")
    list_string = list_string.split(' ')
    return list_string

# Code
initial_list = input_list()
print(f"Ваша последовательность: {initial_list}")
unique_numbers_list = []
for i in initial_list:
    if initial_list.count(i)==1:
        unique_numbers_list.append(i)

if len(unique_numbers_list) < 1:
    print("Ваша последовательность состоит из повторяющихся элементов")
else:
 print(f"Cписок неповторяющихся элементов заданной последовательности: {unique_numbers_list}")