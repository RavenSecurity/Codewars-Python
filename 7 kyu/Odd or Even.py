def odd_or_even(arr):
    result = 0
    for x in arr:
        result = result + x
    if result % 2 == 0:
        return "even"
    else: return "odd"