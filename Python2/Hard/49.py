class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    def greet(self):
        super().greet() 

def main():
    c = C()
    c.greet()  
    try:
        A.greet() 
    except TypeError as e:
        print(f"TypeError: {e}")

main()
