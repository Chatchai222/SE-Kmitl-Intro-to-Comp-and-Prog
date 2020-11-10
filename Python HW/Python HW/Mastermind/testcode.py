import tkinter as tk

def change_mes(mesbox, newtext):
    print("Hello")
    first_frame.place_forget()
    mesbox.pack(for)

root = tk.Tk()

mesbox = tk.Message(root, text="Hello")
mesbox.pack()

first_frame = tk.Frame(root, bg="Yellow")
first_frame.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)

second_frame = tk.Frame(root, bg="Green")
second_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)

fire_frame = tk.Frame(root, bg="Red")
fire_frame.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.2)


my_button = tk.Button(root,text="Click me", command=lambda: change_mes(mesbox, "stinky"))
my_button.pack()


root.mainloop()