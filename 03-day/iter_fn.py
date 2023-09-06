name = 'ABC'
print(name, name[0])
# name[0] = 'j'
my_str_iterator = iter(name)

print(next(my_str_iterator))
print('Hell yeah')
print(next(my_str_iterator))
print(next(my_str_iterator))
# StopIteration
# print(next(my_str_iterator))
my_str_iterator = iter(name)

roles = ('user', 'admin', 'sysadmin')
roles_iter = iter(roles)
# for i in roles:
#     print(i)
for i in roles_iter:
    print(i)

print(next(roles_iter))
