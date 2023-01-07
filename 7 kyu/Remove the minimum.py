def remove_smallest(numbers):
    result = [*numbers]
    if numbers == []:
        return []
    else:
        result.remove(min(result))
    return result
#     raise NotImplementedError("TODO: remove_smallest")