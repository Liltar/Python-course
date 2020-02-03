# 1: count each symbol in a string 'spam and eggs or eggs with spam'
string = 'spam and eggs or eggs with spam'
import collections

print(collections.Counter(string))
#
# 2 Дан отсортированный список. Реализуйте бинарный поиск.
#
# 3 palyndrome check
# ERROR (неправильная интерпретация пробелов!!!
# решить проблему
value = input('Enter the phrase to check is it a palindrome:')
value1 = ''.join(reversed(value))
if value == value1:
    print(value, 'is the palindrome')
elif value is None:
    print('No input')
elif:
    print(value, 'is not the palindrome')
#
# 4 На ввод дается строка. Нужно каждое слово развернуть наоборот.
# Порядок слов не должен меняться.
# ERROR (порядок слов меняется!!. а не должен)
value2 = input("Enter a phrase to reverse it:")
reversed_phrase = ''.join(reversed(value2))
print(reversed_phrase)
#
# 5 Напишите генератор случайных паролей.
# После запуска программа должна ждать ввода числа - длины пароля и нажатия Enter.
# Завершить программу нужно если будет введен 0.
# Также нужно проверять является ли введенная строка числом.
# Допустимые символы - цифры, большие и маленькие латинские буквы.
# (нужно использовать метод input)
#import random

#input('Enter length of the intended password')

#
# 6 Дана строка "English = 78 Science = 83 Math = 68 History = 65".
# Вычислить сумму всех чисел в строке.
string1 = 'English = 78 Science = 83 Math = 68 History = 65'
for 
list = (string1)
print(list)
# print(sum_digits(""))
# def sum_digits(digit):