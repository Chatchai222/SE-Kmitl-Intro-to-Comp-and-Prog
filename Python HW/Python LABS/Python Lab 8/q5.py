#Q5
# text = "abcde"
# for y in range(len(text)):
#     for x in range(y, len(text)):
#         print(text[y:x+1:])

def issubset(short, long):
    subset = False

    length_of_short = len(short)
    for x in range(len(long)):
        if short == long[x:x + length_of_short:]:
            subset = True

    return subset

def LCS (s1, s2):
    output = ""
    for x in range(len(s1)):
        for y in range(x, len(s1)):
            #print(s1[x:y+1:])
            test_string = s1[x:y+1:]
            if issubset(test_string, s2):
                if len(test_string) > len(output):
                    output = test_string

    return output

print(LCS("ingenious", "intelligent"))
print(LCS("philosophically", "zoophilous"))
print(LCS("sister", "water"))
print(LCS("other", "another"))
print(LCS("scada", "smart home"))


