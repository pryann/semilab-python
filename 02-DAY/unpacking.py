abc = 'abcdefghi'
a, b, *c = abc
print(a, b, c)

grades_by_students = [1, [2, 3, 4, 5], [1, 1, 2], 4]
s1, (s21, s22, s23, s24), s3, s4 = grades_by_students
print(s1, s21, s22, s23, s24, s3, s4)

# variable1 = 'value'
# variable2 = 'value2'
# variable3 = 'value3'

variable1, variable2, variable3 = 'value', 'value2', 'value3'
