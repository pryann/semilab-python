grade = input('Adj meg egy érdemjegyet: ')
print(type(grade))

# if grade == '1':
#     print('elégtelen')
# elif grade == '2':
#     print('elégséges')
# elif grade == '3':
#     print('közepes')
# elif grade == '4':
#     print('jó')
# elif grade == '5':
#     print('jeles')
# else:
#     print('Ez nem érdemjegy')

grade_dict = {
    '1': 'elégtelen',
    '2': 'elégséges',
    '3': 'közepes',
    '4': 'jó',
    '5': 'jeles'
}

# if grade in grade_dict:
#     print(grade_dict[grade])
# else:
#     print('Ez nem érdemjegy')

# grade_text = grade_dict[grade] if grade in grade_dict else 'Ez nem érdemjegy'
print(grade_dict[grade] if grade in grade_dict else 'Ez nem érdemjegy')
