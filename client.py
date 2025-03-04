from person_hierarchy.person import Person
from person_hierarchy.employee import Employee
from person_hierarchy.customer import Customer

# Create an instance of the Employee class with relevant attributes.
emily = Employee('Emily', 'Ryalls', 26, 'Female', 'Marketing', 20000, 37.5 )
print(emily)

# Calculate the overtime pay for Emily, assuming she worked 2 hours of overtime.
overtime = emily.calculate_overtime_pay(2)
print(overtime)

# Give Emily a raise of 2% (0.02) and calculate the new salary.
new_salary = emily.give_raise(0.02)
print(new_salary)

# Create an instance of the Customer class with relevant attributes (name, age, gender, balance, and purchased items).
maggie = Customer("Maggie", "Smith", 60, "Female", 20550,["Dog food", "Shoes", "Handbag"] )
# Make a new purchase for Maggie, adding "Pineapple" to her purchase list.
new_purchase = maggie.make_purchase("Pineapple")
# Print the updated purchase list after making the new purchase.
print(new_purchase)