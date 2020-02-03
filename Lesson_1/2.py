#2. даны два словаря
# a = {'a': 1, 'b': 4, 't': 67}
# b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}
# 2.1 найти ключи которые есть в обоих словарях
# 2.2 найти ключи которые есть только во 2м словаре, но нет в 1м
# 2.3 объединить словари в один, так чтоб числа при одинаковых ключах суммировались
#
a = {'a': 1, 'b': 4, 't': 67}
b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}
# 2.1 intersection
print(b.keys() + a.keys())
# 2.2
print(b.keys() - a.keys())
# 2.3
print(a.keys() | b.keys())
#
# 3. реализовать разложение числа на степени простых множителей (ввод через input, выход по 0)
# (простое число - делится только на себя и 1)
# вход:
# 456
# 0
# вывод:
# 2^3 * 3 * 19
# 2.1 intersection
a = {'a': 1, 'b': 4, 't': 67}
b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}
dicts = [a, b]