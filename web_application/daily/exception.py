# class Unknow(Exception):
#     pass

# class Val(Unknow):
#     def __init__(self,value1,value2) -> None:
#         self.value1 =value1
#         self.value2 = value2
        
#     def method(self):
#         try:
#            raise Unknow
#         except Unknow as ex:
#             print("an exception has occured")
# obj = Val(2,0)
# obj.method()

class Age(Exception):
    print("hi")

class Valid(Age):
    def __init__(self,t) -> None:
        self.age =t
    def check(self):
        if(self.age<0 or self.age>100):
            try:
                raise Age()
            except Age:
                print("age has to be in between 0 and 100")
obj=Valid(111)
obj.check()

# import logging

# logging.basicConfig(filename='validations_new.log',filemode='a',format = '%(levelname)s:%(asctime)s:%(message)s')  

# class Validations(Exception):
#     def __init__(self, *args: object) -> None:
#         super().__init__(*args)

# class User_data(Validations):
#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age
#     def __call__(self):
#         try:
#             if(len(self.name) <10 or ((self.age) <0 or (self.age) >100)):
#                 raise Validations
#         except Validations as e:
#             logging.exception('the user has entred username of length should be greater than 10 and age should be in between 0 and 100')
#             print("length of variable should be 10",e)
        
      
        
# obj = User_data("aaaaaaaaaaaaa",33) 
# obj()


x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))