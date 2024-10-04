class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self, sound):
           print(sound)

dog = Dog()
dog.speak()  
