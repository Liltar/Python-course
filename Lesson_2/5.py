# 5 Напишите генератор случайных паролей.
# После запуска программа должна ждать ввода числа - длины пароля и нажатия Enter.
# Завершить программу нужно если будет введен 0.
# Также нужно проверять является ли введенная строка числом.
# Допустимые символы - цифры, большие и маленькие латинские буквы.
# (нужно использовать метод input)
import random
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZbacdefghijklmnopqrstuvwxyz0123456789"
value = input('enter password length:')
p =  "".join(random.sample(s, int(value)))
try: if 
print(p)