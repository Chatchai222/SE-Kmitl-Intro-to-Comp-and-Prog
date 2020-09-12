# Question 5
user_input = int(input("Input your amount of money: "))
bank_notes_list = [[1000, 0],
                   [500, 0],
                   [100, 0],
                   [50, 0],
                   [20, 0],
                   [10, 0],
                   [5, 0],
                   [2, 0],
                   [1, 0]]
# This part is for the calculation of amount of banknotes for each bank notes
for each_bank_note in bank_notes_list:
    amount_of_notes = user_input // each_bank_note[0]  # // gives only quotient (int division)
    each_bank_note[1] = amount_of_notes
    user_input = user_input % each_bank_note[0]

# Printing out the amount
for each_bank_note in bank_notes_list:
    if each_bank_note[1] == 0:
        continue
    elif each_bank_note[0] > 10:
        text = str(each_bank_note[0]) + "-Baht notes: " + str(each_bank_note[1])
    else:
        text = str(each_bank_note[0]) + "-Baht coins: " + str(each_bank_note[1])

    print(text)