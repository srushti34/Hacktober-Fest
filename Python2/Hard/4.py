from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
     pass

def sleep(self):
    print("Sleeping...")

class Dog(Animal):
    def sound(self, volume): 
     print(f"Bark at volume {volume}")

def main():
    try:
     dog = Dog()
     dog.sound() 
     dog.sleep()
    except TypeError as e:
     print(f"TypeError: {e}")

main()