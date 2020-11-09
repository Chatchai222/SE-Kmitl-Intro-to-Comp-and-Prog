def remove_the_third(thelist):
    output = []
    for i, x in enumerate(thelist):
        if (((i + 1) % 3) == 0):
            continue
        output.append(x)

    thelist.clear()
    for y in output:
        thelist.append(y)



list1 = [3,6,6,3,7,2,0,1,5,4]
remove_the_third(list1)
print(list1)
