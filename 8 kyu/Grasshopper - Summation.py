def summation(num):
    result = 0
    count = 1
    
    while count <= num:
        result += count
        count += 1
    return result

    if __name__ == '__main__':
        assert summation(1) == 1
        assert summation(8) == 36