from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name=name
        self.modules=[]
        self.grades={}

    def add_module(self,title):
        self.modules.append(title.get_title())
        self.grades[title.get_title()]=title.get_grade()

    def get_list_modules(self):
        for i in self.modules:
            print(i)
        print ('\n')

    def get_grades(self):
        for keys in self.grades:
            print(keys,':',self.grades[keys])



### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.add_module(math1)
me.add_module(sem)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
