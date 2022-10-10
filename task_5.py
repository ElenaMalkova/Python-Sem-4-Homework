# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
import re


# Превращаем файл в строку
def covert_file(fl):
    with open(fl, 'rt') as mnch_file:
        mnch_str = (mnch_file.readline())
        mnch_str = re.sub(r'(\d)(x.?\d?)( )(.)( )', r'\1\3\4', mnch_str)
    return mnch_str.split(' ')


# Строку делаем числами
def to_integer(mn_list):
    d_j = 0
    for d_i in mn_list:
        def_match = re.search(r'^–', d_i)  # Ищем элемент начинающийся (^) с минуса
        if def_match:  # Если да
            d_i = int(d_i[:0] + d_i[1:])  # Сдвигаем элементы строки на один символ влево и превращаем в int
            d_i *= -1  # Превращаем элемент в отрицательный
        mn_list[d_j] = int(d_i)  # Добавляем в список
        d_j += 1
    return mn_list


mnch_1 = covert_file('polynome1.txt')  # Парсим файлы
mnch_2 = covert_file('polynome2.txt')

to_integer(mnch_1)  # Делаем числами
to_integer(mnch_2)

mnch_result = []  # Список в котором формируется результат сложения в цифрах
j = 0
for i in mnch_1:
    mnch_result.append(i + mnch_2[j])
    j += 1

# К результатам в элементах списка добавляем иксы со степенями
exp = 0  # Степень
max_exp = len(mnch_result) - 1  # Максимальная степень
for exp in range(0, max_exp):  # К каждому элементу дописываем икс в степени
    if exp == len(mnch_result) - 2:
        mnch_result[exp] = str(mnch_result[exp]) + "x"  # Для красоты, последний икс одинокий, а не "x^1"
    else:
        # Строка равна строке с иксом-крышечкой и значением степени
        mnch_result[exp] = str(mnch_result[exp]) + "x^" + str(max_exp)
        max_exp -= 1

# Собираем финальную строку
result_string = ''
index = 0
for val in mnch_result:
    val = str(val)  # Конвертим элементы результирующего списка в строку
    match = re.search(r'^\D\d*', val)  # Ищем отрицательные числа
    if match:
        if index != 0:  # Но только не у самого первого
            minus = re.sub(r'-', r' - ', val)  # подставляем минус как знак, а не атрибут числа
            result_string += minus
        else:
            minus = re.sub(r'-', r'-', val)  # подставляем минус как знак, а не атрибут числа
            result_string += minus
            index += 1
    else:
        if index != 0:
            val = " + " + val  # Плюсы тоже обрамляем пробелами
            result_string += val
        else:
            result_string += val  # Но только не у самого первого
            index += 1

f = open("mn_result.txt", "w")
f.write(result_string)
f.close()

print(f'{mnch_result}\n{result_string}')
