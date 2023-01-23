def square_digits(num):
    return int(''.join(map(str, [int(i)*int(i) for i in str(num)])))