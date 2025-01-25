def length(lst):
    
    if not isinstance(lst, list):
        raise TypeError("Input should be a list")
    return len(lst)
def mean(lst):
   
    if not isinstance(lst, list) or any(not isinstance(x, (int, float)) for x in lst):
        raise TypeError("All elements in the list should be numeric (int or float)")
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    return sum(lst) / len(lst)
def range_of_list(lst):
   
    if not isinstance(lst, list):
        raise TypeError("Input should be a list")
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    return max(lst) - min(lst)
def median(lst):
   
    if not isinstance(lst, list):
        raise TypeError("Input should be a list")
    if not lst:
        raise ValueError("List cannot be empty")
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]
import math

def standard_deviation(lst):
   
    if not isinstance(lst, list) or any(not isinstance(x, (int, float)) for x in lst):
        raise TypeError("All elements in the list should be numeric (int or float)")
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    m = mean(lst)
    variance = sum((x - m) ** 2 for x in lst) / len(lst)
    return math.sqrt(variance)
def list_statistics(lst):
    
    if not isinstance(lst, list):
        raise TypeError("Input should be a list")
    if not lst:
        raise ValueError("List cannot be empty")
    
    return {
        "length": length(lst),
        "mean": mean(lst),
        "range": range_of_list(lst),
        "median": median(lst),
        "standard_deviation": standard_deviation(lst)
    }
numbers = [1, 2, 3, 4, 5]

print("Sample List:", numbers)
print("Length:", length(numbers))  # Output: 5
print("Mean:", mean(numbers))  # Output: 3.0
print("Range:", range_of_list(numbers))  # Output: 4
print("Median:", median(numbers))  # Output: 3
print("Standard Deviation:", standard_deviation(numbers))  # Output: ~1.41
print("List Statistics:", list_statistics(numbers))

# Empty list
empty_list = []
try:
    print("Mean for empty list:", mean(empty_list))
except ValueError as e:
    print(e)

# Single element
single_element_list = [42]
print("List Statistics (Single Element):", list_statistics(single_element_list))

# Negative numbers
negative_list = [-5, -1, -3, -2, -4]
print("List Statistics (Negative Numbers):", list_statistics(negative_list))

# Floating-point numbers
float_list = [1.5, 2.5, 3.5, 4.5, 5.5]
print("List Statistics (Floating-Point Numbers):", list_statistics(float_list))
