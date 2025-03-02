from person_hierarchy.person import Person
from person_hierarchy.employee import Employee
from person_hierarchy.customer import Customer


emily = Employee('Emily', 'Ryalls', 26, 'Female', 'Marketing', 20000, 37.5 )
print(emily)

overtime = emily.calculate_overtime_pay(2)
print(overtime)

new_salary = emily.give_raise(0.02)
print(new_salary)

maggie = Customer("Maggie", "Smith", 60, "Female", 20550,["Dog food", "Shoes", "Handbag"] )
new_purchase = maggie.make_purchase("Pineapple")
print(new_purchase)