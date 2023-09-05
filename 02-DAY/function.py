import random
# from random import randint


def log(message):
    print(f'Message: {message}')

    def inner_fn():
        print('Oh mama!')

    inner_fn()


print(type(log))
log('Csáó bella')

# Higher Order Function


def make_incrementor(n):
    def incrementor(x):
        return n + x

    return incrementor


result = make_incrementor(10)
print(type(result))
print(result(20))
print(make_incrementor(10)(20))


def success_fn(num):
    print(f'SUCCESS: {num}')


def error_fn(num):
    print(f'ERROR: {num}')

# higher order function, callback function


def make_request(successCallback, errorCallback):
    rand_int = random.randint(1, 10)
    if rand_int > 5:
        successCallback(rand_int)
    else:
        errorCallback(rand_int)


make_request(success_fn, error_fn)
