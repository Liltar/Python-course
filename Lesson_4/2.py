# Дан массив целых чисел. Нужно найти сумму элементов с индексами подходящими под правило.
# Правило такое - сумма бит двоичного представления четна.
# Затем перемножить эту сумму и предпоследний элемент исходного массива.
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_l = [bin(i) for i in l]
print(new_l)
new_l1 = [len() for i in new_l]
