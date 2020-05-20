"""
Python OOP
"""

'''
CLASSES:

Whenever we have a use case where we have a number of data points and each data point will
have certain attributes and certain actions that it can preform, then instead of defining
them for each of the data point, we create a class defining those attributes & actions once
and then making each data point an instance of that class. While creating the instance for
a data point, we provide the specific attributes & actions that we want the data point to
be associated with. (hence it is called instance attributes and not class attributes)

For example we have a company that has multiple employees. Each employee will have attributes
like name, age, salary, position etc. and each employee does some sort of action in the
company. So we define a class that acts as a blue print for all the common things about the
employees
'''
class Employee:
    pass

'''
:Difference between a class and an instance of a class:
    class is basically blue print for creating instances
    each instance is a unique set of data point derived from that class.
'''
employee1 = Employee()
employee2 = Employee()
'''
employee1 and employee2 are two separate instances of the same class
>>> print(employee1)
<__main__.Employee instance at 0x1013e7170>
>>> print(employee2)
<__main__.Employee instance at 0x1013e70e0>
we see that they both have separate address space indicating they are both separate instances

- Understanding this difference is key in using instance variables and class variables.
'''

'''
INSTANCE VARIABLE

instance variables contain data that is UNIQUE to each instance.
'''
employee1.first_name = "akshay"
employee1.last_name = "jagtap"
employee1.email = "akshay.jagtap@domain.com"
employee1.pay = 500

employee2.first_name = "test"
employee2.last_name = "user"
employee2.email = "test_user@akamai.com"
employee2.pay = 600
'''
above attributes are same but their values are different for each instance.
'''

'''
It is better to assign attributes and actions to data points when we create its instance.
This is done by using special init method. We can think of this method as an initializing
method. If we want to understand this method comparing to other language, we can think of
this method as a 'constructor'.

When we create methods in a class, the method receives the instance of that class automatically
By convention this instance is called 'self' but we can call it whatever we want.

After self, we can sepcify what other variable attributes & actions we can take as input.
'''
class Employee:
    def __init__(self, first_name, last_name, pay):
        '''init method is were we set all our instance variables.
        also we don't need to take email as argument in this case since we can construct it
        using other arguments.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@domain.com'

'''
When we say self is an instance of the class, doing
>>>...    self.first_name = first_name
is same as doing:
>>>employee1.first_name = 'akshay'
And this attribute will be set automatically when we instanciate a class object for a data point.
'''

'''When we create an instance of a class for a data point, we pass in the instance variable
values. While creating an instance of a class the __init__ method is called / run automatically.
Also the instance is passed automatically to the __init__ method. So when creating the instance
we don't need to pass self as first argument.
'''

'''
In order to add some ability to perform certain actions in a class, we can add methods to that class.
Eg- Action: Ability to print information related to an instance object of that class
We can do something like:
'''
>>> employee1 = Employee('Akshay', 'Jagtap', 5000)
>>> print(
    '{} {} gets paid {} and his email is {}'.format(
        employee1.first_name,
        employee1.last_name,
        employee1.pay,
        employee1.email
    )
)
'''
This is unnecessary and instead we can do something like:
'''
class Employee:
    def __init__(self, first_name, last_name, pay):
        '''init method is were we set all our instance variables.
        also we don't need to take email as argument in this case since we can construct it
        using other arguments.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@domain.com'

    def print_info(self):
        return '{} {} gets paid {} and his email is {}'.format(
            self.first_name,
            self.last_name,
            self.pay,
            self.email
        )
'''
In above code, we created a common method to print the information. This method will work for any
instance object of that class since the print_info method takes current instance as a pointer to
which information is to be used.

Lets try printing:
'''
>>> print(employee1.print_info())
'Akshay Jagtap gets paid 5000 and his email is akshay.jagtap@domain.com'
>>> print(employee2.print_info())
'test user gets paid 5000 and his email is test.user@domain.com'

'''
Notice that we used () when we called print. This is because it is a method that we are calling using
the instance object. If we don't put the () then we will get the method object instead of return value
of the method:
'''
>>> print(employee1.print_info)
<bound method Employee.print_info of <__main__.Employee object at 0x101977b00>>

'''
When we write a method in a class and do not provide the instance (self) to it as a first argument, the
code will compile without issues. However when you call that method using an instance object of that class
You will see an error:
    TypeError: print_info() takes 0 positional arguments but 1 was given
This just means, the instance object (self) was automatically parsed to the method when calling it but the
method was not expecting it. Hence while writing any methods in a class we always need to pass an instance
variable as the first argument to the methods belonging to that class.
'''

'''
self.var1, self.var2 etc are called instance variables. They are set using the self argument and are unique
to every instance object of that class.
'''

"""CLASS VARIABLES"""
'''
Class variables are variables that are shared across all instances of a class. Class variables are same for
each instance.
Lets say with our Employee class example, we have amount of raise same for all employees.
'''
class Employee:
    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + '_' + lastname + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04) # 4% standard raise

'''
In the above code, we are using instance variables to calculate the raise for each employee(instance object
of the class). The way we would use the above code is:
>>> emp_1 = Employee('akshay', 'jagtap', 50000)
>>> emp_2 = Employee('test', 'user', 60000)
>>> emp_1.apply_raise()
>>> emp_1.pay
52000
>>> emp_2.apply_raise()
>>> emp_2.pay
62400
>>> 

There are a few things wrong with this approach:
    We should be able to get something like emp_1.raise_amount OR since it is common to all employees,
    Employee.raise_amount. For that the raise_amount is not an attribute to access. So we cannot update this value
    for all employees even if we wanted.
    If we want to change it we will need to manually do this.
So instead we use class variables and define them inside the class and outside the method like this:
Here we are accessing class variables using class name.
'''
class Employee:

    raise_amount = 1.04 # 4%

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

'''
We can also access class variables using instance attribute example:
'''
def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)

'''
Here you might think, if 'raise_amount' is a class variable, how can we access it using the instance of that class?
If we print:
>>> print(Employee.raise_amount)
1.04
>>> print(emp_1.raise_amount)
1.04
>>> print(emp_2.raise_amount)
1.04

Here is what happened:
We are able to access class variables from both: Class itself as well as from both instances. When we try to access
an attribute on an instance it will first check if the instance contains that attribute. If it doesn't then it will
check if the class or any parent class contains that attribute.
So when we accessed emp_1.raise_amount, it checked if there is an instance attribute called self.raise_amount. Upon
not finding it, it checked if the class Employee() has that attribute or not.

