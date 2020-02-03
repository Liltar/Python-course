# 3 palyndrome check
# ERROR (неправильная интерпретация пробелов!!!
# решить проблему
value = input('Enter the phrase to check is it a palindrome:')
value1 = ''.join(reversed(value))
if value == value1:
    print(value, 'is the palindrome')
    print('No input')
elif value is None:
    pass
else:
    print(value, 'is not the palindrome')