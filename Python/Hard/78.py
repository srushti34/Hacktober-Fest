class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

def main():
    rect = Rectangle(5, 10)
    try:
        print(f"Area: {rect.area()}")
        rect.width = -3 
        print(f"Area after changing width: {rect.area()}")
    except ValueError as e:
        print(f"ValueError: {e}")

main()
