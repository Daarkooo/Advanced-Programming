def length(lst):
    """
    Returns the number of elements in the list.
    If the list is empty, it returns 0.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    return len(lst)


def mean(lst):
    """
    Returns the arithmetic mean of the list.
    If the list is empty, returns None.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    
    if len(lst) == 0:
        return None
    
    total_sum = sum(lst)
    return total_sum / len(lst)


def range_of_list(lst):
    """
    Returns the difference between the max and min values of the list.
    If the list is empty, returns None.
    """
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    
    if len(lst) == 0:
        return None
    
    return max(lst) - min(lst)


# Test Cases
numbers = [1, 2, 3, 4, 5]
empty_list = []
single_element = [5]
negative_numbers = [-1, -2, -3, -4, -5]
floating_points = [1.5, 2.5, 3.5]

# Length Test
print("Length of numbers:", length(numbers))  # Output: 5
print("Length of empty list:", length(empty_list))  # Output: 0

# Mean Test
print("Mean of numbers:", mean(numbers))  # Output: 3.0
print("Mean of empty list:", mean(empty_list))  # Output: None
print("Mean of single element list:", mean(single_element))  # Output: 5.0
print("Mean of floating point numbers:", mean(floating_points))  # Output: 2.5

# Range Test
print("Range of numbers:", range_of_list(numbers))  # Output: 4
print("Range of empty list:", range_of_list(empty_list))  # Output: None
print("Range of negative numbers:", range_of_list(negative_numbers))  # Output: 4
print("Range of floating point numbers:", range_of_list(floating_points))  # Output: 2.0
