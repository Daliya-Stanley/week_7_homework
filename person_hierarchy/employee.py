from person_hierarchy.person import Person

class Employee(Person):
    def __init__(self, firstname, lastname, age, gender, position, joining_salary, weekly_hours):
        super().__init__(firstname, lastname, age, gender)
        self.position = position
        self.__current_salary = joining_salary
        # self.__joining_salary = joining_salary
        # self.__current_salary = current_salary
        # self.__overtime_hours = overtime_hours
        self._weekly_hours = weekly_hours

    def get_position(self):
        return self.position

    # def get_joining_salary(self):
    #     return self.__joining_salary

    def get_current_salary(self):
        return self.__current_salary

    # def get_overtime_hours(self):
    #     return self.__overtime_hours

    def get_weekly_hours(self):
        return self._weekly_hours

    def set_position(self, position):
        if str(position).isalpha():
            self.position = position
        else:
            raise ValueError('Position must be alphabetic')

    # def set_joining_salary(self, joining_salary):
    #     if joining_salary.isfloat():
    #         self.__joining_salary = joining_salary
    #     else:
    #         raise ValueError('Joining salary must be numerical')

    def set_current_salary(self, current_salary):
        if current_salary.isfloat():
            self.__current_salary = current_salary
        else:
            raise ValueError('Current salary must be numerical')

    # def set_overtime_hours(self, overtime_hours):
    #     if overtime_hours.isfloat():
    #         self.__overtime_hours = overtime_hours
    #     else:
    #         raise ValueError('Overtime hours must be numerical')

    def set_weekly_hours(self, weekly_hours):
        if weekly_hours.isfloat():
            self._weekly_hours = weekly_hours
        else:
            raise ValueError('Weekly hours must be numerical')


    def calculate_overtime_pay(self, __current_salary, overtime_hours, _weekly_hours):
        overtime_pay = (self.__current_salary/52/self._weekly_hours)*(1.5 * overtime_hours)
        return f"Overtime pay: £{overtime_pay:.2f}"
        # (hourly rate) * (1.5 x overtime hours)

    def give_raise(self, __current_salary, raise_percentage):
        self.__current_salary = self.__current_salary + (self.__current_salary * raise_percentage)
        return f"The new salary is £{self.__current_salary:.2f}"