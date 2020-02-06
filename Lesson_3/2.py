# 2  Дана строка S. Нужно распечатать её подстроками длиной w. Например S=”ABCDEFGHIJKLIMNOQRSTUVWXYZ” и w=4 - выход
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ
s = 'ABCDEFGHIJKLIMOPQRSTUVWXYZ'
w = 4
for i in range(0, len(s), w):
    print(s[i : i + 4])