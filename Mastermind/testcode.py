import tkinter as tk

def change_mes(mesbox, newtext):
    mesbox['text'] += newtext


root = tk.Tk()
mesbox = tk.Message(root, text="Hello")
mesbox.pack()

my_button = tk.Button(root,text="Click me", command=lambda: change_mes(mesbox, "stinky"))
my_button.pack()


root.mainloop()