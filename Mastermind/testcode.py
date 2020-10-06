

secret = list("royy")
guess = list("ryby")
output = []


new_list = [s + g for s, g in zip(enumerate(secret), enumerate(guess))]
new2_list = zip(enumerate(secret), enumerate(guess))

# For black pegs
black_list = zip(secret, guess)
for each_peg in black_list:
    if each_peg[0] == each_peg[1]:
        output.append('B')
        secret.remove(each_peg[0])
        guess.remove(each_peg[1])

for each_peg in guess:
    for each_secret_peg in secret:
        if each_peg == each_secret_peg:
            output.append('W')
            break



print(output)
print(guess)

