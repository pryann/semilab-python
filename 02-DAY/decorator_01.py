def bacis_decorator(fn):
    def wrapper():
        print('start wrapper')
        fn()
        print('end wrapper')

    return wrapper


def say_hello():
    print('Hi')


bacis_decorator(say_hello)()
