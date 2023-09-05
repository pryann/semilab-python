yearly_salary_list = [120000, 100000, 90000, 55000]
yearly_salary_list_copy = yearly_salary_list

yearly_salary_list.append(99999)
print(yearly_salary_list)
print(yearly_salary_list_copy)

yearly_salary_list_copy = [9, 99, 999]
print(yearly_salary_list)
print(yearly_salary_list_copy)

yearly_salary_list_real_copy = yearly_salary_list.copy()
yearly_salary_list_real_copy = yearly_salary_list[:]
yearly_salary_list_real_copy = list(yearly_salary_list)
print(id(yearly_salary_list) == id(yearly_salary_list_real_copy))
print(yearly_salary_list_real_copy)


mutable_type = [1, 2, 3, 4, 5]


def duplicate_list_items(lista):
    lista = lista[:]
    for i in range(len(lista)):
        lista[i] *= 2
    return lista


duplicate_list_items(mutable_type)
print(mutable_type)


def default_value(lista=None):
    if lista is None:
        lista = []
    lista.append(1)
    return lista


print(default_value())
print(default_value())
print(default_value())
