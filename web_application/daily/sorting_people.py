class Person:
    def __init__(self,firstname,lastname,age) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

class People_sort(Person):
    """
    This class is a child class for Person class.
    It will accept the list and the attribute to sort and finally writes the sorrted list.
    """
    list_to_sort = []

    # this method will sort the values present in the list_to_sort
    def sortingmethod(self):  
        length = len(People_sort.list_to_sort)
        for i in range(0,length-1):
            for j in range(i,length):
                if(People_sort.list_to_sort[i]>People_sort.list_to_sort[j]):
                    temp = People_sort.list_to_sort[i]
                    People_sort.list_to_sort[i] = People_sort.list_to_sort[j]
                    People_sort.list_to_sort[j] = temp

    def __init__(self,list1:list ,value:str) -> None:
        self.sort_list = list1
        self.string_to_sort = value

    # this method will store the valuesin the list_to_sort according to the user choice and return the sorted list
    def sort_the_person(self)->list:  
        if(self.string_to_sort == 'firstname'):
            for val in self.sort_list:
                People_sort.list_to_sort.append(val.firstname)
            self.sortingmethod()
            return (People_sort.list_to_sort)
        elif(self.string_to_sort == 'lastname'):
            for val in self.sort_list:
                People_sort.list_to_sort.append(val.lastname)
            self.sortingmethod()
            return (People_sort.list_to_sort)
        elif(self.string_to_sort == 'age'):
            for val in self.sort_list:
                People_sort.list_to_sort.append(val.age)
            self.sortingmethod()
            return (People_sort.list_to_sort)
        else:
            return "The attribute that you have entred to sort has not found"


p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)

obj1 = People_sort([p1, p2, p3], "firstname")
print(obj1.sort_the_person())
    

    