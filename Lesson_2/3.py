# 3 palyndrome check
# возможна неправильная интерпретация пробелов
# решить проблему
value = input('Enter the phrase to check is it a palindrome:')
value1 = ''.join(reversed(value))
if value == value1:
    print(value, 'is the palindrome')
    print('No input')
else:
    print(value, 'is not the palindrome')