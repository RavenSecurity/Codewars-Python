def sum_two_smallest_numbers(numbers):
    result = []
    result.append(min(numbers))
    numbers.remove(min(numbers))
    result.append(min(numbers))
    numbers.remove(min(numbers))
    sum = result[0] + result[1]
    return sum