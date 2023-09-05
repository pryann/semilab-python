import time


def performance(fn):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        finish = time.perf_counter()
        print(
            f'Function name: {fn.__name__},\nComplete : {finish - start: 0.4f} sec.')
        return result
    return wrapper


@performance
def test(n, m):
    return [[j for j in range(n)] for i in range(m)]


test(10000, 10000)

# https://stackoverflow.com/questions/8710456/reading-a-binary-file-with-python#8711061
