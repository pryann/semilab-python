class Student:
    __slots__ = ['first_name', 'last_name', 'grades', '__neptun_code']

    school = 'Berklee'

    def __init__(self, first_name, last_name, grades, neptun_code):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades
        self.__neptun_code = neptun_code
        # self._neptun_code = neptun_code
    
    def average_grade(self):
        return round(sum(self.grades) / len(self.grades), 2)

    def log_user(self):
        print(f'{self.first_name} {self.last_name} : {self.__neptun_code}')

student = Student('John', 'Doe', [1,2,3,4,4], 'BNM345')
print(student.first_name, student.last_name)

student.first_name = 'Jane'
print(student.first_name)

print(student.average_grade())
print(student.school)

student2 = Student('Jane', 'Doe', [1,1,2,3], 'ABC235')
print(student2.school)
# student.school = 'ELTE'
# print(student.school)
# print(student2.school)

print(Student.school)
Student.school = 'ELTE'
print(student.school)
print(student2.school)

# user.age = 30
# print(user.age)

# error
# print(student.__neptun_code)

student.log_user()
print(student._Student__neptun_code)