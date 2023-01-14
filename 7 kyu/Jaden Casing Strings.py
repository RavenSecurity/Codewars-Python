def to_jaden_case(string):
    a = string.split(' ')
    for i in range(len(a)):
        a[i] = a[i].capitalize()
    return ' '.join(a)