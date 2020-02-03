# 1: count each symbol in a string 'spam and eggs or eggs with spam'
string = 'spam and eggs or eggs with spam'
import collections
print(collections.Counter(string))