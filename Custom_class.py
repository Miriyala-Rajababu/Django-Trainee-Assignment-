Topic: Custom Classes in Python

Description: You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the 
format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}


Answer:

class Rectangle:
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width
        self.index = 0  

    def __iter__(self):
        self.index = 0 
        return self

    def __next__(self):
        if self.index == 0:
            self.index += 1
            return f'length: {self.length}'
        elif self.index == 1:
            self.index += 1
            return f'width: {self.width}'
        else:
            raise StopIteration

length_of_rectangle=input("enther the length of rectagle")
iterable_objects = Rectangle(10, 20)
for x in iterable_objects:
    print(x)
