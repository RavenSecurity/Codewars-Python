def number(lines):
    i = 1
    ordered = []
    for n in lines:
        ordered.append('{}: {}'.format(i, n))
        i += 1
    return ordered
        