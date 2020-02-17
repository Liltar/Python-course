LL = [9, 9, 9, 9]
def counter:
    for i in range(len(LL)):
        if i == i+1:
            LL.count(i)
print(counter(LL))