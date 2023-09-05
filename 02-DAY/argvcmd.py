import sys

argv = sys.argv[1:]
argv_dict = {i.split('=')[0]: i.split('=')[1] for i in argv}
# argv_dict = {}
# for i in argv:
#     key_value = i.split('=')
#     argv_dict[key_value[0]] = key_value[1]

print(argv_dict)
