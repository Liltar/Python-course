'''3
0489899894
0914545454
+912121212

3
05454841
15454448848
45454787787'''

def phones_fixer(func):
    def wrapper(nlist):
        ...
        return func(nlist)
    return wrapper()


@phones_fixer
def sort_numbers(numbers_list):
    return '\n'.join(sorted(numbers_list))

def read_numbers():
    n = int(input())
    numbers = []
    for i in range(n):
        number = input()
        numbers.append(number)
        return numbers

if __name__ == '__main__':
    numbers = read_numbers()
    print(sort_numbers(numbers))

