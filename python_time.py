#Run w/  python3 test.py

#def test():
#    "Stupid test function"
#    L = []
#    for i in range(100):
#        L.append(i)
#
#if __name__=='__main__':
#    from timeit import Timer
#    t = Timer("test()", "from __main__ import test")
#    print t.timeit()


def f(x):
    return x**2
def g(x):
    return x**4
def h(x):
    return x**8

import timeit
print(timeit.timeit('[func(42) for func in (f,g,h)]', globals=globals()))
