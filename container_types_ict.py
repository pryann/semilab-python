user = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 33,
    'hobbies': ['reading', 'playing games']
}

print(user['first_name'])
print(user['hobbies'][0])
user.update({'first_name': 'Jane', 'sex': 'female'})
print(user)

user.pop('age')
print(user)
