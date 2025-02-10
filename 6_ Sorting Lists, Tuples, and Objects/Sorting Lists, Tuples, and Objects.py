# List
li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li,reverse=True)
print(s_li)

li.sort(reverse=True)
print(li)

li = [-6,-5,-4,1,2,3]
s_li = sorted(li,key=abs)
print(s_li)

# Tuple
tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print(s_tup)

# Dictionary

di = {'name':'Corey','job':'Programming','age':'None','os':'Mac'}
s_di = sorted(di)
print(s_di)

# Object
class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

from operator import  attrgetter

e1 = Employee('Carl',37,70000)
e2 = Employee('Sarah',29,80000)
e3 = Employee('Jhon',43,90000)

employees = [e1,e2,e3]

# def e_sort(emp):
#     return emp.salary
#
# s_emp = sorted(employees,key=e_sort,reverse=True)
# s_emp = sorted(employees,key=lambda e: e.name,reverse=True)
s_emp = sorted(employees,key=attrgetter('age'),reverse=True)

print(s_emp)


