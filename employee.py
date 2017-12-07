from vehicle import *
from customer import *

class Employee(object):
    emp_id=0

    def __init__(self, name):
        self.__name=name
        self.__id=Employee.emp_id
        Employee.emp_id += 1

    def __str__(self):
        return '%s is of type %s'%(self.__name,self.get_title())
    ######## CODE MISSING HERE

    def get_name(self):
        return self.__name

    
    def get_title(self):
        return 'Subordinate'
    ######## CODE MISSING HERE
    
class Manager(Employee):

    def get_title(self):
        return 'Manager'
    ######## CODE MISSING HERE

    def get_sales_report(self,salesman):
        try:
            print('%s current cumulative sales %d'%(salesman.get_name(),salesman.sales[salesman]))
        except KeyError as err:
            print('KeyError: salesman doesnt have any sales jet')
    ######## CODE MISSING HERE

class Salesman(Employee):

    sales={}

    def sale(self,vehicle,sales_price,customer):
        if customer.credit_score()==True:
            if self in Salesman.sales:
                Salesman.sales[self] += sales_price
            else:
                Salesman.sales[self]=sales_price
        else:
            print('Customer does not have enough credit score')



### test cases ###

## initialising employee instances

Eric = Manager("Eric")
Kyle = Employee("Kyle")
Stan = Salesman("Stan")
Kenny = Salesman("Kenny")
Craig = Salesman("Craig")

## printing employee instances

print(Eric) # expected output: Employee: Eric is of type Manager
print(Kyle) # expected output: Employee: Kyle is of type Subordinate
print(Stan) # expected output: Employee: Stan is of type Subordinate
print(Kenny) # expected output: Employee: Kenny is of type Subordinate
print(Craig) # expected output: Employee: Craig is of type Subordinate


## registering sales

Kenny.sale(Veh2,6000,Heidi)

Stan.sale(Veh1,9000,Wendy)


## printing an individual sales report:
print(Kenny)
#print(Salesman.sales)

Eric.get_sales_report(Kenny)
Eric.get_sales_report(Stan)
# expected output:
# Kenny's current cumulative sales:
# 6000


