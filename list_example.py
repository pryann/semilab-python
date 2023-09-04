yearly_salaries = [1e5, 120000, 90000, 250000, 160000]
# 0b1011, 0o67, 0x1aF

# sum, avg, min, max

# for ciklusváltozó in interabe:
#     ciklusmag

# for i in range(len(yearly_salaries)):
#     print(f'{i}: {yearly_salaries[i]}')


def summa_yearly_salary(salarie_list):
    summa = 0
    for salary in salarie_list:
        summa += salary
    return summa


def avarage_yearly_salary(salarie_list):
    return summa_yearly_salary(salarie_list) / len(salarie_list)


def min_salary(salarie_list):
    if len(salarie_list) == 0:
        return
    min_value = float('inf')
    for salary in salarie_list:
        if salary < min_value:
            min_value = salary
    return min_value


print(min(yearly_salaries))


def is_even(num):
    return 'even' if num % 2 == 0 else 'odd'


print(is_even(7))

result = summa_yearly_salary(yearly_salaries)
print(result)

print(dir(__builtins__))
