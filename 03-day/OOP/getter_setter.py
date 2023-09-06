class Employee:
    def __init__(self, name: str, job: str, yearly_salary:int) -> None:
        self.name = name
        self.job = job
        self.__yearly_salary = yearly_salary

    def get_salary(self):
        return round(self.__yearly_salary, 2)

    def set_salary(self, value):
        yearly_salary_max_limit = 120000
        if value > yearly_salary_max_limit:
            self.__yearly_salary = yearly_salary_max_limit
        else:
            self.__yearly_salary = value
        # self.__yearly_salary = yearly_salary_max_limit if value > yearly_salary_max_limit else value


bubu = Employee('Mr. Bubu', 'doctor', 100000)
print(bubu.get_salary())
bubu.set_salary(150000)
print(bubu.get_salary())