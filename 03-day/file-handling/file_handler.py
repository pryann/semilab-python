from os import chdir, path

# print('__file__:', __file__) # full abs path
# print('path.dirname(__file__):', path.dirname(__file__)) # without file
# print('path.join(path.dirname(__file__), "files")', path.join(path.dirname(__file__), 'files'))
chdir(path.join(path.dirname(__file__), 'files'))

# with open('primarchs.txt', 'r') as file:
#     print(file.read())
#     print(file.read()) # pointer a végén

with open(file='primarchs.txt', mode='r', encoding='utf-8') as file:
    # read one line
    # print(file.readline()) 

    for line in file:
        for char in line:
            print(char)
    file.seek(0)
    print(file.read())

with open(file='primarchs2.txt', mode='a', encoding='utf-8') as file:
    users = ['John', 'Jane']
    for user in users:
        file.write(user + '\n') # felülírja a tartalmat