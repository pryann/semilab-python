def bacis_decorator(fn):
    def wrapper():
        print('start wrapper')
        fn()
        print('end wrapper')

    return wrapper


@bacis_decorator
def say_hello():
    print('Hi')


say_hello()

# bacis_decorator(say_hello)()
