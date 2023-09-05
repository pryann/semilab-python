def bacis_decorator(fn):
    def wrapper(name):
        print('start wrapper')
        fn(name)
        print('end wrapper')

    return wrapper


@bacis_decorator
def say_hello(name):
    print(f'Hi {name}')


say_hello('John Doe')
# bacis_decorator(say_hello)()
