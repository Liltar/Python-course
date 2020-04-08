# Дается строка - нужно проверить является ли она валидным паролем:
# (1) длина больше 4 символов,
# (2) содержит только маленькие латинские буквы и цифры,
# (3) число букв должно быть нечетным, а цифр четным.
password = input('Enter a password:')
# 1 длина больше 4 символов
if len(password) > 4:
    print('password is ok')
else:
    raise Exception('Length of password should be more than 4')

# The length was:

# 2 содержит только маленькие латинские буквы и цифры
# import string
# string.ascii_lowercase
condition_1 = list('abcdefghijklmnopqrstuvwxyz')
condition_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in password:

    print('Good')
else:
    raise Exception('Wrong symbol')
# if i in password:
#    i = condition_1 and i = condition_2
#    print('password is ok')
