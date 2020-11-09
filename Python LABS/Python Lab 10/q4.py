first_list = [3,1,1,1,2,7]
second_list = [4,1,1,2,2,5]
output_list = []

def get_the_difference(first_list, second_list):
    output_list = []
    for each_element in first_list:
        if not(each_element in second_list):
            output_list.append(each_element)

    for each_item in second_list:
        if not(each_item in first_list):
            output_list.append(each_item)

    return output_list

print(get_the_difference([3,1,1,1,2,7], [4,1,1,5]))