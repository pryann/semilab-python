set_elements = {1, 2, 3}
set_elements.add(3)
print(set_elements)

# TypeError
# print(set_elements[0])

set_elements.remove(1)
print(set_elements)

x1 = {'a', 'b', 'c'}
x2 = {'b', 'c', 'd'}
print(x1.union(x2))
print(x1 | x2)
print(x1.union(x2))
print(x1.intersection(x2))
print(x1 & x2)
print(x1.difference(x2))
print(x1 - x2)
