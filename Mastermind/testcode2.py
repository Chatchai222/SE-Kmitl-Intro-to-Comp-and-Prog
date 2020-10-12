import random
possible_code = 'ROYGBV'
secret_code = 'HELLO'
new_secret = ""
for _ in range(4):
    new_secret += random.choice(possible_code)

secret_code = new_secret
print(secret_code)