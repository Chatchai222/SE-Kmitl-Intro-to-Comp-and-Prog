"""
This program is the game mastermind!
- In this game the user will be the code breaker
"""
import tkinter as tk

# GUI part of the mastermind
HEIGHT = 700
WIDTH = 1000

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

main_frame = tk.Frame(root, bg='white')
main_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

code_frame = tk.Frame(main_frame, bg='Yellow')
code_frame.place(relx=0, rely=0, relheight=0.8, relwidth=0.7)

key_frame = tk.Frame(main_frame, bg='Black')
key_frame.place(relx=0.7, rely=0, relheight=0.8, relwidth=0.3)

status_box = tk.Text(main_frame, bg='Green')
status_box.place(relx=0.75, rely=0.825, relheight=0.15, relwidth=0.2)

entry_bar = tk.Entry(main_frame, bd=3)
entry_bar.place(relx=0.1, rely=0.85, relheight=0.05, relwidth=0.3)

enter_code_button = tk.Button(main_frame, text='Enter code')
enter_code_button.place(relx=0.125, rely=0.925, relheight=0.05, relwidth=0.1)

restart_button = tk.Button(main_frame, text='Restart')
restart_button.place(relx=0.275, rely=0.925, relheight=0.05, relwidth=0.1)

root.mainloop()
