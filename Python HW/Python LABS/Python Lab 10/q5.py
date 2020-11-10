def my_sort(num_list):
    l = []
    l.append(num_list[0])

    for x in num_list[1::]:
        index = 0 # This is index of l
        largest_num = True
        for y in l:
            if x <= y:
                l.insert(index, x)
                largest_num = False
                break
            index += 1

        if largest_num:
            l.append(x)

    return l


print(my_sort([4,3,2,10,12,1,5,6,-5]))
