import threading
import time

def  my():
    for i in range(5):
        print("hi")
        time.sleep(1)

def me():
    for j in range(5):
        print("Hello")
        time.sleep(1)


my_thread = threading.Thread(target=my)
me_thread = threading.Thread(target=me)
my_thread.start()
time.sleep(1)
me_thread.start()

my_thread.join()

my_thread.join()

print("process ended")

abstact methods
import abc
from abc import ABC,abstractmethod

class Polygon(ABC):
 
    @abstractmethod
    def noofsides(self):
        print("in abstarct method")
        pass

class Triangle(Polygon):
 
    # overriding abstract method
    
    def noofsides(self):
        super().noofsides
        print("I have 3 sides")

try:
    k = Triangle()
    k.noofsides()

except Exception as err:
    print(err)


list1  = [1,2,4]
list2 =  [1,3,4]

method 1
list3 = (list1+list2)
list3.sort()
print("method 1",list3)

# methd 2
list3 = list1+list2
for i in range(len(list3)-1):
    for j in range(i+1,len(list3)):
        if(list3[i]>list3[j]):
            temp = list3[i]
            list3[i] = list3[j]
            list3[j] = temp
print("method 2",list3)

temp1 = list(list1)
temp2 = list(list2)

for value in temp2:
    for i in range(len(temp1)):
        if(value<=temp1[i]):
            temp1.insert(i,value)
            break
    else:
        temp1.append(value)
print(temp1)









import multiprocessing

def  my():
    print("hi")

def me():
    print("Hello")


my_thread = multiprocessing.Process(target=my)
me_thread = multiprocessing.Process(target=me)

if __name__ == '__main__':
    my_thread.start()
    me_thread.start()

    my_thread.join()
    my_thread.join()

    print("program is done")

import weakref,gc

class Hi:
    def __del__(self):
        print("iam called ")

    def m1(self):
        print("in use")
obj = Hi()
obj.m1()
d = weakref.WeakValueDictionary()
d['weak'] = obj
print(d['weak'])
del obj
print(gc.collect)
print(d['weak'])


import logging

logging.debug('this is a debug msg')


