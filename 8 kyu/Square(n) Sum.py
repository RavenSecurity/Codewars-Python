def square_sum(numbers):
    # your code here
    arr = []

    for x in numbers:
        arr.append(x * x)

    return sum(arr)