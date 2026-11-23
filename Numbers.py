# Numbers.py

# Create a list of numbers
numbers = [2, 4, 4, 6, 8, 10]

# 1. Sum of numbers in the list
def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# 2. Average / Mean of numbers in the list
def average_numbers(numbers):
    total = sum_numbers(numbers)
    average = total / len(numbers)
    return average

# 3. Median and Mode of numbers in the list
def median_and_mode(numbers):
    # MEDIAN
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2

    if n % 2 == 1:
        median = sorted_numbers[middle]
    else:
        median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

    # MODE
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    highest = max(counts.values())
    mode = [num for num, count in counts.items() if count == highest]

    if len(mode) == 1:
        mode = mode[0]

    return median, mode

# Print results for the list
print("List:", numbers)
print("Sum:", sum_numbers(numbers))
print("Average/Mean:", average_numbers(numbers))
print("Median & Mode:", median_and_mode(numbers))
