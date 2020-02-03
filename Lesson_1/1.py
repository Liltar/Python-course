#дан список [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
# 1.1 найти максимум, минимум и их индексы в массиве
# 1.2 найти три самых часто встречаемых элемента массива
# 1.3 преобразовать в список где каждое значение будет встречаться только 1 раз
 #1.3.1 порядок не сохранялся
 #1.3.2 порядок сохранялся#
# 1.1 найти максимум, минимум и их индексы в массиве
number = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
print('the largest number is', max(number), 'and its index is', number.index(max(number)))
print('the smallest number is', min(number), 'and its index is', number.index(min(number)))
# 1.2 найти три самых часто встречаемых элемента массива
import collections
print('three most common numbers and their frequency are', collections.Counter(number).most_common(3))
#1.3.1 порядок не сохранялся
print(set(number))
# 1.3.2
print(list(collections.Counter(number)))