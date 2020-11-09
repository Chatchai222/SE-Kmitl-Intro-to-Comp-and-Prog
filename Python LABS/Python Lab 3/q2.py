# Question 2
import unicodedata

user_input = input("Please enter a character: ")
my_unicode = (ord(user_input))
my_unicode = "{:04x}".format(my_unicode)

my_string = 'The Unicode of "' + str(user_input) + '" is u' + str(my_unicode) + "."
print(my_string)
# print("{:04x}".format(100))

