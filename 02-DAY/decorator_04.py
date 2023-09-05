def bacis_decorator(fn):
    def wrapper(a, b):
        value = fn(a, b)
        # return value
        return value * 1.27

    return wrapper


@bacis_decorator
def summa(a, b):
    return a + b


print(summa(10, 20))
# bacis_decorator(say_hello)()
