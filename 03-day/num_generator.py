import sys

nums_generator = (i * i for i in range(100_000_000))
print(f'size: {sys.getsizeof(nums_generator)}')
print(f'sum: {sum(nums_generator)}')
print(f'sum: {sum(nums_generator)}')


nums_lst = [i * i for i in range(100_000_000)]
print(f'size: {sys.getsizeof(nums_lst)}')
print(f'sum: {sum(nums_lst)}')
print(f'sum: {sum(nums_lst)}')
