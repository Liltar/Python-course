# Дан массив. Реализовать функцию которая будет переставлять 2 выбранных элемента списка местами.
# Функция должна иметь вид: def swap(target_list, item_index1, item_index2).
def swap(list, item_index1, item_index2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
# Driver function
target_list = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swap(target_list, pos1 - 1, pos2 - 1))