# 4 На ввод дается строка. Нужно каждое слово развернуть наоборот.
# Порядок слов не должен меняться.
value = input("Enter a phrase to reverse it:")
def reverseWordSentence(Sentence):
    return ' '.join(word[::-1] for word in Sentence.split(" "))
print(reverseWordSentence(value))