def bubble_sort(user_list):
    swap = True
    while (swap):
        for x in range(1,len(user_list)):
            swap = False
            if (user_list[x] <= user_list[x-1]):
                user_list[x], user_list[x-1] = user_list[x-1], user_list[x]
                swap = True


list1 = [3,2,9,7,8]
bubble_sort(list1)
print(list1)