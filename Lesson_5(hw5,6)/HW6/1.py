#1
L = [2, 2, 4, 4, 4, 6, 6, 7, 9, 9, 9, 9, 5, 5, 1]
LL = [9, 9, 9, 9]
for i in range(len(L)):
    if i == i+1:
        L.count(i)
    elif i != i + 1:
        L.count(i)


#print(list(collections.Counter(ll).most_common(LL)))

#print(list(collections.Counter(L).most_common(L)))