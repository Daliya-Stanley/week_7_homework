from person_hierarchy.person import Person

class Employee(Person):
    def __init__(self, firstname, lastname, age, gender, position, joining_salary, current_salary, overtime):
        super().__init__(firstname, lastname, age, gender)
        self.position = position
        self.__joining_salary = joining_salary
        self.__current_salary = current_salary
        self.__overtime = overtime

    def get_position(self):
        return self.position

    def get_joining_salary(self):
        return self.__joining_salary

    def get_current_salary(self):
        return self.__current_salary

    def get_overtime(self):
        return self.__overtime

    def set_position(self, position):
        if str(position).isalpha():
            self.position = position
        else:
            raise ValueError('Position must be alphabetic')

    def set_joining_salary(self, joining_salary):
        if joining_salary.isfloat():
            self.__joining_salary = joining_salary
        else:
            raise ValueError('Joining salary must be numerical')

    def set_current_salary(self, current_salary):
        if current_salary.isfloat():
            self.__current_salary = current_salary
        else:
            raise ValueError('Current salary must be numerical')

    def set_overtime(self, overtime):
        if overtime.isfloat():
            self.__overtime = overtime
        else:
            raise ValueError('Overtime must be numerical')






    def set_current_salary(self):
        return self.__current_salary

    def set_overtime(self):
        return self.__overtime


