import random
import numpy as np

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= 0:  
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

    def shuffle_data(self):
        try:
            self.data = list(np.random.shuffle(self.data)) 
        except Exception as e:
            print("Shuffle error:", e)

def main():
    rev = Reverse("Python")
    rev.shuffle_data()
    for char in rev:
        print(char, end=" ")

    random_num = random.choice(rev.data) 
    print("\nRandom character from reversed data:", random_num)

main()
