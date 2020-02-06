import collections
import heapq
# Есть список. Нужно реализовать операцию левый и правый сдвиг на указанный шаг. Нужно решение с deque и без него.
# Пример списка [1, 2, 3, 4, 5]  сдвиг влево на 4 для него даст [5, 1, 2, 3, 4].
l = []
n = int(input("N: "))
while True:
    L = input("L: ")
    if L == "0":
        break
    l.append(L)
left = list(l)
for _ in range(n):
    v = left.pop(0)
    left.append(v)
print('left shift', left)

right = list(l)
#right shift
for _ in range(n):
    v = right.pop()
    right.insert(0, v)
print('right shift', right)