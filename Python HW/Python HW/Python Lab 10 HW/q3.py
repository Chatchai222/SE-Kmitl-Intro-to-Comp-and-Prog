def my_union(list1,list2):
    output_list = list1.copy()
    for num in list2:
        if num in output_list:
            continue
        else:
            output_list.append(num)

    return output_list

def my_intersection(list1, list2):
    output_list = []
    for num in list1:
        if num in list2:
            output_list.append(num)

    return output_list

def my_difference(list1,list2):
    output_list = []
    for num in list1:
        if num in list2:
            continue
        else:
            output_list.append(num)

    return output_list

list1 = [3,1,2,7]
list2 = [4,1,2,5]
print(my_union(list1, list2))
print(my_intersection(list1,list2))
print(my_difference(list1,list2))
print(list1)
print(list2)