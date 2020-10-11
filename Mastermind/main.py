"""
This program is the game mastermind!
- In this game the user will be the code breaker
"""
import tkinter as tk

# The decodeboard class which contains all the required methods, game, GUI
class DecodeBoard:
    def __init__(self):
        self.secret_code = "RRYY"
        self.code_list = []
        self.current_code = []
        self.key_peg_list = []
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=700, width=1000)
        self.main_frame = tk.Frame(self.root, bg="White")
        self.code_frame = tk.Frame(self.main_frame, bg="#D0F2F4")
        self.key_frame = tk.Frame(self.main_frame, bg="Grey")
        self.status_box = tk.Message(self.main_frame)
        self.entry_frame = tk.Frame(self.main_frame, bg="Grey", bd=2)
        self.input_frame = tk.Frame(self.main_frame)
        self.enter_code_button = tk.Button(self.main_frame, text="Enter code", command=lambda: self.press_enter_code())
        self.restart_button = tk.Button(self.main_frame, text="Restart", command=lambda: self.display_code_list())
        self.red_button = tk.Button(self.input_frame, text="R - Red", fg="Red", command=lambda: self.press_color("Red", "R"))
        self.orange_button = tk.Button(self.input_frame, text="O - Orange", fg="Orange", command=lambda: self.press_color("Orange", "O"))
        self.yellow_button = tk.Button(self.input_frame, text="Y - Yellow", fg="Yellow", command=lambda: self.press_color("Yellow", "Y"))
        self.green_button = tk.Button(self.input_frame, text="G - Green", fg="Green", command=lambda: self.press_color("Green", "G"))
        self.blue_button = tk.Button(self.input_frame, text="B - Blue", fg="Blue", command=lambda: self.press_color("Blue", "B"))
        self.violet_button = tk.Button(self.input_frame, text="V - Violet", fg="Violet", command=lambda: self.press_color("Violet", "V"))
        self.clear_code_button = tk.Button(self.input_frame, text="Clear code", command=lambda: self.press_clear_code())

    def display_key_peg_list(self):
        x_coord = [0.04, 0.28, 0.52, 0.76]
        y_coord = [0.04, 0.2, 0.36, 0.52, 0.68, 0.84]
        for y, pegs in zip(y_coord, self.key_peg_list):
            for x, peg in zip(x_coord, pegs):
                peg.place(relx=x, rely=y, relheight=0.12, relwidth=0.2)

    def display_code_list(self):
        print(self.code_list)
        print("Used display_code_list")
        x_coord = [0.04, 0.28, 0.52, 0.76]
        y_coord = [0.04, 0.2, 0.36, 0.52, 0.68, 0.84]
        for y, code_guess in zip(y_coord, self.code_list):
            for x, code_peg in zip(x_coord, code_guess):
                code_peg.place(relx=x, rely=y, relheight=0.12, relwidth=0.2)
                print("Placed a peg" + str(x))

    def display_current_code(self):
        coord = [0, 0.25, 0.5, 0.75]
        code_with_coord = zip(self.current_code, coord)
        for each_peg, each_coord in code_with_coord:
            each_peg.place(relx=each_coord, rely=0, relwidth=0.24, relheight=1)

    def generate_key_peg(self):
        output = []
        secret = list(self.secret_code)
        guess = [peg['text'] for peg in self.current_code]
        # For black_pegs
        black_list = list(zip(secret, guess))
        for peg_tuple in black_list:
            if peg_tuple[0] == peg_tuple[1]:
                output.append(tk.Label(self.key_frame, text='B', bg="Black"))
                secret.remove(peg_tuple[0])
                guess.remove(peg_tuple[1])

        for peg in guess:
            if peg in secret:
                secret.remove(peg)
                output.append(tk.Label(self.key_frame, text="W", bg="White"))


        self.key_peg_list.append(output)

    def press_color(self, in_color, in_text):
        self.current_code.append(tk.Label(self.entry_frame, text=in_text, bg=in_color, fg=in_color))
        self.display_current_code()
        print(self.current_code)

    def press_clear_code(self):
        self.current_code = []
        clear_frame = tk.Frame(self.entry_frame, bg="Grey")
        clear_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        print(self.current_code)
        print("Hello")

    def press_enter_code(self):
        if len(self.current_code) < 4:
            self.status_box['text'] = "Please input all 4 codes"
            return 0

        self.status_box['text'] = ""
        self.current_code = self.current_code[:4:]

        # IDK why tkinter don't allow to change parent/master of the widget so I have to just append a new widget
        self.code_list.append([tk.Label(self.code_frame, bg=code_peg['bg'], text=code_peg['text']) for code_peg in self.current_code])
        self.generate_key_peg()
        self.press_clear_code()
        self.display_code_list()
        self.display_key_peg_list()



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
board = DecodeBoard()

board.canvas.pack()
board.main_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
board.code_frame.place(relx=0, rely=0, relheight=0.8, relwidth=0.7)
board.key_frame.place(relx=0.7, rely=0, relheight=0.8, relwidth=0.3)
board.status_box.place(relx=0.75, rely=0.825, relheight=0.15, relwidth=0.2)
board.entry_frame.place(relx=0.1, rely=0.85, relheight=0.05, relwidth=0.3)
board.input_frame.place(relx=0.45, rely=0.85, relheight=0.125, relwidth=0.2)
board.enter_code_button.place(relx=0.125, rely=0.925, relheight=0.05, relwidth=0.1)
board.restart_button.place(relx=0.275, rely=0.925, relheight=0.05, relwidth=0.1)
board.red_button.place(relx=0, rely=0, relheight=0.25, relwidth=0.5)
board.orange_button.place(relx=0, rely=0.25, relheight=0.25, relwidth=0.5)
board.yellow_button.place(relx=0, rely=0.5, relheight=0.25, relwidth=0.5)
board.green_button.place(relx=0.5, rely=0, relheight=0.25, relwidth=0.5)
board.blue_button.place(relx=0.5, rely=0.25, relheight=0.25, relwidth=0.5)
board.violet_button.place(relx=0.5, rely=0.5, relheight=0.25, relwidth=0.5)
board.clear_code_button.place(relx=0.25, rely=0.75, relheight=0.25, relwidth=0.5)

board.root.mainloop()


