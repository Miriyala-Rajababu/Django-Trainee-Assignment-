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
