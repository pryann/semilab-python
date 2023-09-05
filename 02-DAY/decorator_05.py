def increase_price_by_tax(tax_rate):
    def decorator(fn):
        def wrapper(a, b):
            price = fn(a, b)
            increased_value = price * (1 + tax_rate / 100)
            return increased_value
        return wrapper
    return decorator


def apply_discount(discount):
    def decorator(fn):
        def wrapper(*argv, **kwargv):
            price = fn(*argv, **kwargv)
            return (1 - discount / 100) * price
        return wrapper
    return decorator


@increase_price_by_tax(27)
@apply_discount(10)
def summa(a, b):
    return a + b


print(summa(100, 1000))
# bacis_decorator(say_hello)()
