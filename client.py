from person_hierarchy.person import Person
from person_hierarchy.employee import Employee

emily = Employee('Emily', 'Ryalls', 26, 'Female', 'Marketing', 20000, 30000, 37.5 )
print(emily)

overtime = emily.calculate_overtime_pay(
print(overtime)

new_salary = emily.give_raise(30000, 0.02)
print(new_salary)