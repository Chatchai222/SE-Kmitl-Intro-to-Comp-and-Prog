# This is for the game part

def place_key_pegs(user_secret, user_guess):
    print("HEllo")
    output = []
    secret = list(user_secret)
    guess = list(user_guess)

    # For black pegs
    black_list = zip(secret, guess)
    #PRINT

    for i, each_peg in enumerate(black_list):
        print(each_peg, i)
        if each_peg[0] == each_peg[1]:
            output.append('B')
            secret.pop(i)
            guess.pop(i)

    print("Passed black peg")
    print(output)

    # For white pegs
    for each_secret_peg in secret:
        for each_peg in guess:
            if each_peg == each_secret_peg:
                output.append('W')
                break

    return output


#print(place_key_pegs("RRBY", "BBRY"))
def v2(in_guess, in_secret):
    guess = list(in_guess)
    secret = list(in_secret)
    output = []

    # For black pegs
    black_list = list(zip(in_guess, in_secret))
    for each in black_list:
        if each[0] == each[1]:
            output.append("B")
            guess.remove(each[0])
            secret.remove(each[1])

    # For white pegs
    for peg in guess:
        if peg in secret:
            secret.remove(peg)
            output.append("W")






    print("output is", output)

v2("ARRA", "BAAD")

