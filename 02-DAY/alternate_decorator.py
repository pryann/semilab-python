from math import pi


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


def alternate_summa_with_tax_and_discount(price_1, price_2, tax_rate=0, dicount=0):
    return (price_1 + price_2) * (1 + tax_rate / 100) * (1-dicount / 100)


# def alternate_summa_with_tax(price_1, price_2, tax_rate):
#     return (price_1 + price_2) * (1 + tax_rate / 100)


# def alternate_summa_with_discount(price_1, price_2, dicount):
#     return (price_1 + price_2) * (1-dicount / 100)


# PI = 3.14
print(pi)
