def calculate_average(numbers):
 total_sum = 0
 for number in numbers:
    total_sum += number
 average = total_sum / (len(numbers) - 1)
 return average
numbers = [10, 20, 30, 40, 50]
avg = calculate_average(numbers)
print("The average is:", avg)