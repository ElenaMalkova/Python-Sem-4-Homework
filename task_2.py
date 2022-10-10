# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import math
n = int(input("Введите целое положительное число n: "))
prime_factors = []

for i in range(2, math.ceil(n**0.5)+1):
    while n % i == 0:
        prime_factors.append(i)
        n = n/i

if len(prime_factors) < 1:
    print("Это простое число")
else:
    print(f"Список простых множителей числа n: {prime_factors}")