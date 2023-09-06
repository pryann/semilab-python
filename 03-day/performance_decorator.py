from time import perf_counter as pf
# import time as t
import numpy


def performance(fn):
    def wrapper(*args, **kwargs):
        start = pf()
        result = fn(*args, **kwargs)
        finish = pf()
        print(
            f'Function name: {fn.__name__},\nComplete : {finish - start: 0.10f} sec.')
        return result
    return wrapper


@performance
def test(n, m):
    return [[j for j in range(n)] for i in range(m)]


@performance
def generate_nump(n, m):
    numpy.zeros((n, m))


@performance
def generate_nump_2(n, m):
    numpy.empty((n, m))


test(10000, 10000)
res1 = generate_nump(10000, 10000)
res2 = generate_nump_2(10000, 10000)
print(type(res1))
