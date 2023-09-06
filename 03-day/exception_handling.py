import sys


def fn():
    try:
        name = 'Béla'
        # name += 5
        namee += 'Gizi'
    except (NameError):
        print('NameError')
    except (TypeError):
        print('TypeError')
    except:
        print(sys.exc_info())


fn()
print('end')


def calculate(n, m):
    try:
        if n > 1000:
            raise Exception('n is too high')
        return n * m
    except:
        print(sys.exc_info())
        return calculate(1000, m)


print(calculate(1100, 1000))
