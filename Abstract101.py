#import necessary modules 
from abc import ABC, abstractmethod

#create base class
class Abslass(ABC):

    #function to print a value

    def print(self,x):
        print("passed value:" ,x)


     #abstract method 
    @abstractmethod
    def task(self):
        print("we are inside Absclass task ")


#create sub class
class test_class(Abslass):
    def task(self):
        print("we are inside test_class task")


#object of test_class created 
test_obj = test_class()
test_obj.task()
test_obj.print(100)
