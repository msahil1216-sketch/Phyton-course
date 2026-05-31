# import necessary package
from abc import ABC, abstractmethod
# Create a base class
class Animal(ABC):

    # Abstract method
    # should be implemented by all sub classes
    def move(self):
        pass

# Sub classes
class Human(Animal):

    def move(self):
        print("I can walk and run")

class Snake(Animal):

    def move(self):
        print("I can slither")

class Dog(Animal):

    def move(self):
        print("I can bark")

class Lion(Animal):

    def move(self):
        print("I can roar")

#Driver code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()