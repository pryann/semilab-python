salary_tuple = (100000, 90000, 50000, 100000)

print(salary_tuple[0])
print(type(salary_tuple))

# salary_tuple[0] = 110000
print(salary_tuple.count(100000))

salary_list = list(salary_tuple)
salary_list.append(120000)
salary_tuple = tuple(salary_list)

one_size_tuple = (1000, )
print(type(one_size_tuple))
