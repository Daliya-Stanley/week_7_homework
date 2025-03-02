class Person:
    def __init__(self, firstname, lastname, age, gender):
        self.__firstname = firstname.capitilize()
        self.__lastname = lastname.capitilize()
        self.__age = int(age)
        self.__gender = gender.upper()
       # self.__address = address

    def get_firstname (self):
        return self.__firstname

    def get_lastname (self):
        return self.__lastname

    def get_age (self):
        return self.__age

    def get_gender (self):
        return self.__gender

    # def get_address (self):
    #     return self.__address

    def set_firstname (self, firstname):
        if str(firstname).isalpha():
            self.__firstname = firstname
        else:
            raise ValueError ('First Name must be alphabetic')

    def set_lastname(self, lastname):
        if str(lastname).isalpha():
            self.__lastname = lastname
        else:
            raise ValueError('Last Name must be alphabetic')

    def set_age(self, age):
        if age.is_integer():
            self.__age = age
        else:
            raise ValueError('Age must be a number')

    def set_gender(self, gender):
        if str(gender).isalpha():
            self.__gender = gender
        else:
            raise ValueError('Gender must be alphabetic')

   # def set_address(self, address):
       # if str(gender).isalpha():
       #     self.__gender = gender
       # else:
       #     raise ValueError('Gender must be alphabetic')

    def __str__(self):
        return f"First name: {self.__firstname} Last name: {self.__lastname} Age: {self.__age} Gender: {self.__gender}"






