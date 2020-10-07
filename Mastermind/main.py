"""
This program is the game mastermind!
- In this game the user will be the code breaker
"""
import tkinter as tk


def add_code_to_frame(relheight=0.1):
    my_range = [0.1, 0.3, 0.5, 0.7]
    for y in my_range:
        for x in my_range:
            code_peg = tk.Frame(code_frame, bg="White")
            code_peg.place(relx=x, rely=y, relheight=0.1, relwidth=0.1)
            my_label = tk.Label(code_frame, text="Hello")
            my_label.pack()

# GUI part of the mastermind
HEIGHT = 700
WIDTH = 1000

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

main_frame = tk.Frame(root, bg="White")
main_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

code_frame = tk.Frame(main_frame, bg="Yellow")
code_frame.place(relx=0, rely=0, relheight=0.8, relwidth=0.7)

key_frame = tk.Frame(main_frame, bg="Black")
key_frame.place(relx=0.7, rely=0, relheight=0.8, relwidth=0.3)

status_box = tk.Text(main_frame, bg="Green")
status_box.place(relx=0.75, rely=0.825, relheight=0.15, relwidth=0.2)

entry_bar = tk.Entry(main_frame, bd=3)
entry_bar.place(relx=0.1, rely=0.85, relheight=0.05, relwidth=0.3)

enter_code_button = tk.Button(main_frame, text="Enter code", command=add_code_to_frame)
enter_code_button.place(relx=0.125, rely=0.925, relheight=0.05, relwidth=0.1)

restart_button = tk.Button(main_frame, text="Restart")
restart_button.place(relx=0.275, rely=0.925, relheight=0.05, relwidth=0.1)

input_frame = tk.Frame(main_frame)
input_frame.place(relx=0.45, rely=0.85, relheight=0.125, relwidth=0.2)

red_button = tk.Button(input_frame, text="R - Red", fg="Red")
red_button.place(relx=0, rely=0, relheight=0.25, relwidth=0.5)

orange_button = tk.Button(input_frame, text="O - Orange", fg="Orange")
orange_button.place(relx=0, rely=0.25, relheight=0.25, relwidth=0.5)

yellow_button = tk.Button(input_frame, text="Y - Yellow", fg="#EFEC00")
yellow_button.place(relx=0, rely=0.5, relheight=0.25, relwidth=0.5)

green_button = tk.Button(input_frame, text="G - Green", fg="Green")
green_button.place(relx=0.5, rely=0, relheight=0.25, relwidth=0.5)

blue_button = tk.Button(input_frame, text="B - Blue", fg="Blue")
blue_button.place(relx=0.5, rely=0.25, relheight=0.25, relwidth=0.5)

violet_button = tk.Button(input_frame, text="V - Violet", fg="Violet")
violet_button.place(relx=0.5, rely=0.5, relheight=0.25, relwidth=0.5)

clear_code_button = tk.Button(input_frame, text="Clear code")
clear_code_button.place(relx=0.25, rely=0.75, relheight=0.25, relwidth=0.5)

root.mainloop()


