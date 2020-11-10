def print_table(list1):
    new_list = [[str(element) for element in x] for x in list1] # Convert everything to string
    len_set = len(new_list[0])
    longest_len = []
    for i in range(len_set):
        max_list = [len(y[i]) for y in new_list]
        longest_len.append(max(max_list))

    for z in new_list:
        output = ""
        for index, items in enumerate(z):
            output = output + (f"%-{longest_len[index] + 1}s" % items)

        print(output)


list1 = [["X", "Y"], [0, 0], [10, 10], [200, 200]]
list2 = [["ID", "Name", "Surname"],
         ["001", "Guido", "van Rossum"],
         ["002", "Donald", "Knuth"],
         ["003", "Gordon", "Moore"]]
print_table(list1)
print()
print_table(list2)

