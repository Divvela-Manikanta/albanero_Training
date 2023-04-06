# in1 = 2
# while(in1>0):
#     print("hi")
  
# else:
#     print("hello")


# Building the calculator using list and functions
# def Add(*argv):
#     sum = 0
#     for val in argv:
#         sum = sum + val
#     return sum

# def sub(*argv):
#     sum = 0
#     for val in argv:
#         sum = sum - val
#     return sum

# li = [Add(11,333,3),sub(2,4,5,6,8)]
# print(li[1])

# length = 0
# x=['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
# def find_length(x):
#     global length
#     length1=0
#     for j in x:
#         length1+=len(j)
#     return length1

# print(len(x))
# for i in x:
#     if(len(x)==1):
#         length+=1
#     else:
#         length+=find_length(i)

# print(length)



# li=['foo','jppp']
# li[1:1] = ['jiii'] # it has to be in the form of list 
# print(li)
# li.remove('foo') # only take single argument 
# li.extend('iiii')
# print(li)

# li=['2','3','6']
# li2=li+(2,)
# print(li2)

# s1 = {'1','2','3'}
# s2 = {'2','6'}

# k= s1.symmetric_difference(s2)
# s1.update(s2)
# print(s1)
# print(k)                    



# def roots(val,key=2):
#     return val**key 
# print(roots(2))
# print(roots(2,3))
# print(roots(2,4))
# print(roots(2,5))

# print(roots(val=3,key=3))

# import time

# start = time.time()
# print('starting time',start)

# squares = list(map(lambda x: x**2, range(10)))

# end = time.time()

# print("executed in ",float(end-start))


# import sys

# in1 = input("hi")

# print(sys.argv[1])

# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

# print(len(basket))

# di = {'name':'mani','age':23}
# val = list(di.keys())
# print(val)
# for ke in val:
#     print(ke,':',di[ke])

# for k,v in di.items():
#     print(k,v)

# import fib

# print(fib.febn(1))
# fib.val
# fib.fff

# pi = 22/7   
# print(f'{pi:.3f}')


# with open('users.csv') as f:
#     read_data = f.read()
#     print(read_data)
# f.closed



# while True:
#     try:
#         in1 = int(input("enter the number"))
#         k=11/0
#     except ValueError:
#         print("something went worng")
#         break
#     except Exception as ex:
#         print(ex)

# try:
#   raise Exception('hii')
# except Exception as e:
#     print('jii',e)
#     print(e.args)
#     raise TypeError("Expected a number") from e
    
# else:
#     print("code exceuted without exception")


# import timeit 


# class Employee(Exception):
#    def __init__(self) :
#       return None

# class check:
#    global employee_list
#    employee_list = ['mani','hii','hello','xyz']
#    def valid(self,name) ->None:
#       try:
#          if(name not in employee_list):
#             raise Employee()
#       except Employee as e:
#          print('the employee is not avaliable in qqqq company',e)
#       return 'hi'
# obj = check()
# value = (obj.valid('hi'))

# print(obj.valid.__annotations__)

# print(timeit.timeit(value,1))


import reprlib

print(reprlib.repr(set('qqqq1wdeeweeqdfwfvvofvbvbeyrefbvf')))


