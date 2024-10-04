def filter_even_numbers(numbers):
    try:
        evens = [num for num in numbers if num % 2 == 0]  
        return evens
    except TypeError as e:
        print(f"TypeError: {e}")

def main():
    numbers = [1, 2, 3, "four", 5, 6] 
    filtered_numbers = filter_even_numbers(numbers)
    print(f"Filtered Numbers: {filtered_numbers}")

main()
