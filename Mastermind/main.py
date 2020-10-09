"""
This program is the game mastermind!
- In this game the user will be the code breaker
"""
import tkinter as tk

# Classes
class DecodeBoard:
    def __init__(self):
        self.code_list = []
        self.current_code = []
        self.key_peg_list = []

    def display_current_code(self):
        coord = [0, 0.25, 0.5, 0.75]
        code_with_coord = zip(self.current_code, coord)
        for each_peg, each_coord in code_with_coord:
            each_peg.place(relx=each_coord, rely=0, relwidth=0.24, relheight=1)

    def press_color(self, entry_frame, in_color, in_text):
        self.current_code.append(tk.Label(entry_frame, text=in_text, bg=in_color, fg=in_color))
        self.display_current_code()
        print(self.current_code)


    def press_clear_code(self, entry_frame):
        self.current_code = []
        clear_frame = tk.Frame(entry_frame, bg="Grey")
        clear_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        print(self.current_code)
        print("Hello")

    def press_enter_code(self, entry_frame, status_box):
        if len(self.current_code) < 4:
            status_box['text'] = "Please input all 4 codes"
            return 0

        status_box['text'] = ""
        self.current_code = self.current_code[:4:]
        self.code_list.append(self.current_code)
        self.press_clear_code(entry_frame)

        print(self.code_list)




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


# GUI part of the mastermind
HEIGHT = 700
WIDTH = 1000
my_decode_board = DecodeBoard()

root = tk.Tk()
root.title("Mastermind!!!")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

main_frame = tk.Frame(root, bg="White")
main_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

code_frame = tk.Frame(main_frame, bg="Yellow")
code_frame.place(relx=0, rely=0, relheight=0.8, relwidth=0.7)

key_frame = tk.Frame(main_frame, bg="Black")
key_frame.place(relx=0.7, rely=0, relheight=0.8, relwidth=0.3)

status_box = tk.Message(main_frame)
status_box.place(relx=0.75, rely=0.825, relheight=0.15, relwidth=0.2)

entry_frame = tk.Frame(main_frame, bg="Grey", bd=2)
entry_frame.place(relx=0.1, rely=0.85, relheight=0.05, relwidth=0.3)

input_frame = tk.Frame(main_frame)
input_frame.place(relx=0.45, rely=0.85, relheight=0.125, relwidth=0.2)

enter_code_button = tk.Button(main_frame, text="Enter code", command=lambda: my_decode_board.press_enter_code(entry_frame, status_box))
enter_code_button.place(relx=0.125, rely=0.925, relheight=0.05, relwidth=0.1)

restart_button = tk.Button(main_frame, text="Restart")
restart_button.place(relx=0.275, rely=0.925, relheight=0.05, relwidth=0.1)

red_button = tk.Button(input_frame, text="R - Red", fg="Red", command=lambda: my_decode_board.press_color(entry_frame, "Red", "R"))
red_button.place(relx=0, rely=0, relheight=0.25, relwidth=0.5)

orange_button = tk.Button(input_frame, text="O - Orange", fg="Orange", command=lambda: my_decode_board.press_color(entry_frame, "Orange", "O"))
orange_button.place(relx=0, rely=0.25, relheight=0.25, relwidth=0.5)

yellow_button = tk.Button(input_frame, text="Y - Yellow", fg="Yellow", command=lambda: my_decode_board.press_color(entry_frame, "Yellow", "Y"))
yellow_button.place(relx=0, rely=0.5, relheight=0.25, relwidth=0.5)

green_button = tk.Button(input_frame, text="G - Green", fg="Green", command=lambda: my_decode_board.press_color(entry_frame, "Green", "G"))
green_button.place(relx=0.5, rely=0, relheight=0.25, relwidth=0.5)

blue_button = tk.Button(input_frame, text="B - Blue", fg="Blue", command=lambda: my_decode_board.press_color(entry_frame, "Blue", "B"))
blue_button.place(relx=0.5, rely=0.25, relheight=0.25, relwidth=0.5)

violet_button = tk.Button(input_frame, text="V - Violet", fg="Violet", command=lambda: my_decode_board.press_color(entry_frame, "Violet", "V"))
violet_button.place(relx=0.5, rely=0.5, relheight=0.25, relwidth=0.5)

clear_code_button = tk.Button(input_frame, text="Clear code", command=lambda: my_decode_board.press_clear_code(entry_frame))
clear_code_button.place(relx=0.25, rely=0.75, relheight=0.25, relwidth=0.5)

root.mainloop()


