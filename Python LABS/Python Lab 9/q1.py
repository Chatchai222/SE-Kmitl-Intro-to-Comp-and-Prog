import tkinter as tk

def plus(thelabel):
    thelabel['text'] = str(int(thelabel['text']) + 1)

def minus(thelabel):
    thelabel['text'] = str(int(thelabel['text']) - 1)

def reset(thelabel):
    thelabel['text'] = '0'

root = tk.Tk()

count_up = tk.Button(root, text='+', command=lambda: plus(num_label))
count_up.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.25)

count_down = tk.Button(root, text='-', command=lambda: minus(num_label))
count_down.place(relx=0.5, rely=0.3333, relwidth=0.5, relheight=0.25)

reset_button = tk.Button(root, text="Reset", command=lambda: reset(num_label))
reset_button.place(relx=0.5, rely=0.6666, relwidth=0.5, relheight=0.25)

num_label = tk.Label(root, text='0')
num_label.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.25)

root.mainloop()

