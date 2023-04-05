values = [1, 4, 9, 16, 25]

values.append(111)
print(values)
reverse_list = values[::-1]
print(reverse_list)

li = '\'[1,2,3,4]\''
print(repr(li))

def even_odd(val):
    if(val%2==0):
        print("The given number %d is even"%(val))
    else:
        print("The given number %d is odd"%(val))


if __name__ =='__main__':
    input1 = int(input("enter the input"))
    even_odd(input1)


list1 = [1,2,3,4,5]
list2 =[3,45,6,7,6]
for l1,l2 in zip(list1,list2):
    print(f"The value in list1 is {l1} and value in list2 is {l2}")


for i,val  in enumerate(list1):
    print(i,val)


class even_odd:
    def __init__(self,val):
        self.val = val
    def check(self):
        print("hi")
        # value = self.val
        # if(value%2==0):
        #     return("even")
        # else:
        #     return("the given number %d is odd"%(value))

input1 = int(input("enter the number to check: "))
print()
obj1 = even_odd(input1)
print(obj1.check())


class calling:
    count = 0
    print(count)
    def __init__(self):
        calling.count = calling.count + 1
    def mani(self):
        print("hi")

s1 = calling()
s2 = calling()
s3 = calling()
print(s1.mani())


class main:
    def __init__(self):
        print( "hello")
xf = main
while True:
    xf()



class fun:
    name1 = 'mani'
    name2 = 'hi'
ob1 = fun()
fun.name1 = 'changed'
print(ob1.name1)


class test:
    def __init__(self):
        self.a1 = 'apple'
        self.a2 = 'banana'
        self.li = []
    def inserted(self,val):
        self.li.append(val)

obj=test()
print(obj.a1)
obj.inserted(2)
print(obj.li)


def new_method(self,x,y):
    return min(x,x+y)
class c:
    f = new_method
    h = f
obj = c()
print(obj.h(2,4))


class multiple_methods:
    def name(self):
        print("In 1st method")
    def addname(self):
        print("In 2nd method")
obj = multiple_methods()
obj.name()

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
    def show(self):
        print(self.data)

obj1 = Bag()
obj1.addtwice(2)
obj1.show()

class Add:
    def add(self,val1,val2):
        return sum(int(val1),int(val2))
class Accepting(Add):
    def divide(self,val1,val2):
        return val1/val2
obj1 = Accepting()
print(obj1.add(2,3))
print(obj1.divide(2,2))


class main:
    __value=10
    def show(self):
        print(self.__value)
obj1 = main()
try:
    print(obj1.__value)
finally:
    print("executed")


class Employee:
    __count = 0;

    def __init__(self):
        Employee.__count = Employee.__count + 1

    def display(self):
        print("The number of employees", Employee.__count)


emp = Employee()
emp2 = Employee()
try:
    print(emp.__count)
finally:
    emp.display()

class Employee:
    def __init__(self, name, age, position):
        self.name = name # public varaible
        self._age = age  # private variable
        self.__position = position # protected variable

    # Method to show the personal details of the employee
    def personal_details(self):
        return f"The employee name is {self.name} having age of {self._age}"

    # Method to show the working details of the employee
    def qualification(self):
        return f"The employee name is {self.name} having postion of {self.__position}"

manikanta = Employee("mani", 22, "data engineer")
print(manikanta.personal_details())
print(manikanta.qualification())
print(manikanta.name)
print(manikanta._age)
print(manikanta.__position)

import pandas as pd
try:
    # df = pd.read_excel('gsgdjcbe.xlsx')
    raise Exception('code cannot excute further')
except Exception as ex:
    print("exception ",ex)


def check():
    try:
        return True
    finally:
        return False
check()


class dog:
    species = 'xyz' # class variable

    def __init__(self,name,age) :
        self.name = name # instance varaible
        self.age = age
    def show(self):
        print(f"Dog name is {self.name} and having age of {self.age}")
        

dog1 = dog('aaaaa',22)
dog2 = dog('bbbbb',33)     
dog1.species = 'mmmm'
print(dog.species)