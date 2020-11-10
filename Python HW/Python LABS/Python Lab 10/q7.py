
def merge(list1, list2):
    # output_list = []
    # for item in list2:
    #     output_list.append(item)

    output_list = list2[:]

    for x in list1:
        index = 0
        largest_num = True
        for y in output_list:
            if x <= y:
                output_list.insert(index, x)
                largest_num = False
                break
            index += 1

        if largest_num:
            output_list.append(x)

    return output_list


list2 = [2,4,5,6]
print(merge([1,5,16,61,111],list2))

print(list2)