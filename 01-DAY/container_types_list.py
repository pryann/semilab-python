# indexelt, rendezett, duplikált elemek lehetnek benne
salary_list = [100000, 90000, 120000]
print(salary_list[0])
# print(salary_list[3])

salary_list[0] = 200000
print(salary_list[0])

print(len(salary_list))
print(len('sdsdsd'))

print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 2)
print(10 in [1, 2, 3])

salary_list.insert(0, 99999)
print(salary_list.__len__())

print(salary_list.reverse())

print(salary_list)

print(salary_list.count(99999))

salary_list.sort(reverse=True)
print(salary_list)

names_list = ['John', 'Jane', 'Jonny']
names_str = ''.join(names_list)
print(names_list, names_str)
names_list_copy = names_str.split()
print(names_list_copy)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(len(matrix))

print(matrix[2][1])
