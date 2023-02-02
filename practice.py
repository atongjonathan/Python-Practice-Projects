import math

def square_numbers(numbers):
    result = 0
    for number in numbers:
        result += number ** 2
    print(result)

square_numbers([1,2,2])