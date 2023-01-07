def remove_smallest(numbers):
    result = [*numbers] #  == spread operator in Javascript, used to avoid mutation of input
    if numbers == []:
        return []
    else:
        result.remove(min(result))
    return result
    # raise NotImplementedError("TODO: remove_smallest")