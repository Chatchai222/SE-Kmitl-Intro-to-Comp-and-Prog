import random

# Prototype
# def add_code_to_frame():
#     my_range = [0.1, 0.3, 0.5, 0.7]
#     for y in my_range:
#         for x in my_range:
#             code_peg = tk.Frame(code_frame, bg="White")
#             code_peg.place(relx=x, rely=y, relheight=0.1, relwidth=0.1)
#             my_label = tk.Label(code_frame, text="Hello")
#             my_label.pack()
#
#
# def display_current_code(current_code):
#     coord = [0, 0.25, 0.5, 0.75]
#     code_with_coord = zip(current_code, coord)
#     for each_peg, each_coord in code_with_coord:
#         each_peg.place(relx=each_coord, rely=0, relwidth=0.2, relheight=1)
#
# def press_color(current_code, entry_frame):
#     current_code.append(tk.Frame(entry_frame, bg="Red"))
#     display_current_code(current_code)

possible_code = 'ROYGBV'
secret_code = 'HELLO'
new_secret = ""
for _ in range(4):
    new_secret += random.choice(possible_code)

secret_code = new_secret
print(secret_code)