def print_full_name(a, b):
    print('')

# if __name__ == '__main__':
# print("Hello {0} {1}! You just delved into python.".format(input(''), input('')))
file = open(r'D:\Lesson_9\2.txt')
for line in file:
    line1 = line.split()
    # print(line1)
    # print(line1[1][0])
    if line1[1][0] in ['C', 'K']:
        print(line1)

l2 = []