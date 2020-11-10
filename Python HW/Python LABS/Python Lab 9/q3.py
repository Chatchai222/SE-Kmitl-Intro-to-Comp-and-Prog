import tkinter as tk

def haha(event):
    print(f"Mouse pos is {event.x} and {event.y}")
    thecanvas.create_oval(event.x, event.y, event.x+1, event.y+1, fill='blue')

def haha2(event):
    print(f"The key is {event.key}")

def clear_screen(canvas):
    canvas.delete('all')

root = tk.Tk()

thecanvas = tk.Canvas(root, bg='grey')
thecanvas.place(relx=0, rely=0, relwidth=1, relheight=0.7)

describe_label = tk.Label(root, text='Drag the mouse to draw')
describe_label.place(relx=0.1, rely=0.7, relwidth=0.9, relheight=0.1)

clear_button = tk.Button(root, text='Clear', command=lambda: clear_screen(thecanvas))
clear_button.place(relx=0.5, rely=0.8, relwidth=0.2, relheight=0.1)

thecanvas.bind("<B1-Motion>", haha)
thecanvas.bind("<Key>", haha2)

root.mainloop()

