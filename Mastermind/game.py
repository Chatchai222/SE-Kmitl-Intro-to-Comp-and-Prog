# This is for the game part

def place_key_pegs(user_secret, user_guess):

    output = []
    secret = list(user_secret)
    guess = list(user_guess)

    # For black pegs
    black_list = zip(secret, guess)
    for each_peg in black_list:
        if each_peg[0] == each_peg[1]:
            output.append('B')
            secret.remove(each_peg[0])
            guess.remove(each_peg[1])

    # For white pegs
    for each_peg in guess:
        for each_secret_peg in secret:
            if each_peg == each_secret_peg:
                output.append('W')
                break

    return output


playing = True
print(place_key_pegs("ROYY", "RYBY"))



