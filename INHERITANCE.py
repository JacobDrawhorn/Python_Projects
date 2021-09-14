
# parent class
class User:
    name = 'No Name Provided'
    email = ' '
    password = '1234abcd'
    account_number = 0

# child class
class Employee(User):
    base_pay = 11.00
    department = 'General'

# child class
class Customer(User):
    mailing_address = ' '
    mailing_list = True