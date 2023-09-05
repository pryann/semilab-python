# a = 100000
# b = 100000

# print(id(a) == id(b))

# b = 20
# print(id(a) == id(b))


a = 10


def double_num(num):
    print(f'id of num: {id(num)}')
    num = 20
    print(f'id of num after mod: {id(num)}')
    return num * 2


print(f'id of a: {id(a)}')
print(double_num(a))
print(f'id of a after fn running: {id(a)}')
