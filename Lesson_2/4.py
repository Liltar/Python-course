# 4 На ввод дается строка. Нужно каждое слово развернуть наоборот.
# Порядок слов не должен меняться.
# ERROR (порядок слов меняется!!. а не должен)
value2 = input("Enter a phrase to reverse it:")
reversed_phrase = ''.join(reversed(value2))
print(reversed_phrase)