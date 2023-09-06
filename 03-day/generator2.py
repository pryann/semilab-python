def generate_id(start):
    id_num = start + 1
    while True:
        if id_num % 3 == 0 or id_num % 11 == 0:
            break
        yield id_num
        id_num += 1


id_generator = generate_id(1)
print(next(id_generator))
print(next(id_generator))
print(next(id_generator))
print(next(id_generator))
print(next(id_generator))
