from functools import reduce

# def increase_by_one(num):
#     return num + 1

increase_by_one = lambda num: num + 1 

print(increase_by_one(10))


def apply(numbers, fn):
    result = []
    for i in numbers:
        result.append(fn(i))
    return result


print(apply([1, 2, 3, 4, 5], increase_by_one))
print(apply([1,2,3,4,5], lambda num : num**2))
print((lambda num : num**num)(3))

def make_inc(n):
    return lambda x : n ** x

print(make_inc(10)(2))


salaries = [10000,12000,30000,40000, 50000]
salaries_plus = [i * 1.1 for i in salaries]
salaries_plus = list(map(lambda i: i * 1.1, salaries))

low_salries = [i for i in salaries if i < 30000]
print(low_salries)
low_salries = list(filter(lambda i : i < 30000, salaries))
print(low_salries)

multiply_salaries = reduce(lambda a, b : a * b, salaries)
print(multiply_salaries)


arb = list(
    map(lambda num : num ** 3, 
        filter(lambda num : num % 3 == 0, 
               range(100)))
)

print(arb)