#Q4
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
gender = input("Please enter your gender(m/f): ")

username = (gender + last_name[0] + first_name[:6:]).upper()
print(username)