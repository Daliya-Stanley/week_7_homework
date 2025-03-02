from person_hierarchy.person import Person


class Customer(Person):
    def __init__(self,firstname, lastname, age, gender, customer_id, purchase_history):
        super().__init__(firstname, lastname, age, gender)
        self.__customer_id = customer_id
        self.__purchase_history = purchase_history


    def get_customer_id(self):
        return self.__customer_id


    def get_purchase_history(self):
        return self.__purchase_history


    def set_customer_id(self,customer_id):
        if customer_id.is_integer():
            self.__customer_id = customer_id
        else:
            raise ValueError('Customer ID must be numerical')

    def make_purchase(self, item):
        self.__purchase_history.append(item)
        return f"The purchase history of customer includes:{self.__purchase_history}"

