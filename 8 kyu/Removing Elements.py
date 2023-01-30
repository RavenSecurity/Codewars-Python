def remove_every_other(my_list):
    i = len(my_list)
    if i != 0:
        del my_list[1]
        i -= 1
    return my_list