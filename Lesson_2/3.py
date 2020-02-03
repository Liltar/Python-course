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