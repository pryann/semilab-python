def generate_abc():
    yield 'a'
    yield 'b'
    yield 'c'


abc_generator = generate_abc()
print(next(abc_generator))
print(next(abc_generator))
print(next(abc_generator))


for i in generate_abc():
    print(i)

id_generator = (num for num in range(1, 4))

print(type(id_generator))
