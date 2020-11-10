#Q3


def issubset(short, long):
    subset = False

    length_of_short = len(short)
    for x in range(len(long)):
        print(long[x:x+length_of_short:])
        if short == long[x:x+length_of_short:]:
            subset = True

    return subset




