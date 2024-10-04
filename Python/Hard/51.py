class CustomError(Exception):
      pass

def read_file(filename):
     try:
        with open(filename, 'r') as file:
         data = file.read()
         return process_data(data)
     except FileNotFoundError:
         raise CustomError(f"File {filename} not found")
     except CustomError as e:
          print(f"CustomError occurred: {e}")

def process_data(data):
     try:
         numbers = [int(x) for x in data.split(",")]
         return calculate_average(numbers)
     except ValueError:
         raise CustomError("Data contains non-numeric values")

def calculate_average(numbers):
     return sum(numbers) / len(numbers) 

filename = "data.txt"
result = read_file(filename)
print("Average:", result)