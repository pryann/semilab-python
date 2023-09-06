

# The Python __len__ method returns a positive integer
# that represents the length of the object on which it is called.
# It implements the built-in len() function. For example,
# if you call len(x) an object x,
# Python internally calls x.__len__() to determine the length of object x.


class A:
    def __len__(self):
        return 42


a = A()
print(a.__len__())
print(len(a))
