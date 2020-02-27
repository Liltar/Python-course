# Сортировать список от меньшего к большему с помощью heapq
import heapq
l = [['Krishna', 67, 68, 69], ['Arjun', 70, 98, 63], ['Malika', 52, 56, 60]]
heapq.heapify(l)
print([heapq.heappop(l), heapq.heappop(l), heapq.heappop(l)])