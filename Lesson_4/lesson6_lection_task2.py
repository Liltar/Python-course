import time
def timer(f):
    print(f)
    cache = {}
    def tmp(*args):
        cache
        res = f(*args)
        return res
    return tmp
@timer
def func(x, y):
    l = []
    for i in range(y):
        l.append(x)
func(0, 10_000_000)

#decorator remember