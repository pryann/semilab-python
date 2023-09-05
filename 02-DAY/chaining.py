def add_cheese(burger):
    burger['cheese'] = True
    return burger


def add_double_meal(burger):
    burger['doubleMeal'] = True
    return burger


def remove_onion(burger):
    burger['onion'] = False
    return burger


def add_gluten_free_bun(burger):
    burger['glutenFreeBun'] = True
    return burger


def make_burger(basic_burger, *funcs):
    print(type(funcs))
    for fn in funcs:
        basic_burger = fn(basic_burger)
    return basic_burger


user_burger = make_burger({}, add_cheese,
                          add_double_meal, add_gluten_free_bun)
print(user_burger)
