# Statistics Exercise

import math

def get_number():
    while True:
        user_input = input("Enter a numbers separated by commas: ")
        try:
            numbers = [float(x.strip()) for x in user_input.split(",")]
            if not numbers:
                raise ValueError("Empty list")
            return numbers
        except ValueError:
            print("enter a number")


def cal_minimum(numbers):
    return  min(numbers)

def cal_maximum(numbers):
    return max(numbers)

def cal_average(numbers):
    return sum(numbers) / len(numbers)

def cal_variance(numbers):
    mean = cal_average(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance

def cal_deviation(numbers):
    variance = cal_variance(numbers)
    std_dev = math.sqrt(variance)
    return std_dev

def print_result(numbers):
    minimum = cal_minimum(numbers)
    maximum = cal_maximum(numbers)
    average = cal_average(numbers)
    variance = cal_variance(numbers)
    standard_deviation = cal_deviation(numbers)

    print("\n Statistics Report")
    print("-" * 40)
    print(f"Numbers Entered: {numbers}")
    print(f"Count: {len(numbers)}")
    print(f"Min: {round(minimum, 2)}")
    print(f"Max: {round(minimum, 2)}")
    print(f"Average: {round(average, 2)}")
    print(f"Variance: {round(variance, 2)}")
    print(f"Standard Deviation: {round(standard_deviation, 2)}")



if __name__ == "__main__":
    nums = get_number()
    print_result(nums)

