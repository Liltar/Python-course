# 1.1
number = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]
print('the largest number is', max(number), 'and its index is', number.index(max(number)))
print('the smallest number is', min(number), 'and its index is', number.index(min(number)))
# 1.2
import collections
print('three most common numbers and their frequency are', collections.Counter(number).most_common(3))
#1.3.1
import random


# 1.3.2
print(list(collections.Counter(number)))
# 2.1 intersection
a = {'a': 1, 'b': 4, 't': 67}
b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}
dicts = [a, b]