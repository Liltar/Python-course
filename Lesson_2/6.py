# 6 Дана строка "English = 78 Science = 83 Math = 68 History = 65".
# Вычислить сумму всех чисел в строке.
string1 = 'English = 78 Science = 83 Math = 68 History = 65'
def sum_digits(digit):
    return sum(int(x) for x in digit if x.isdigit())
print(sum_digits(string1))
