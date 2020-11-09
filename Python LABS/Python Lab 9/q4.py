import tkinter as tk
from tkinter import messagebox
import random

def mouse_outside_scream(event):
    #messagebox.showwarning("Warning", "Mouse pointer is not in the rectangle")
    print(f"IN root x is {event.x} y is {event.y}")
    my_canvas.create_rectangle(10,10, 360, 210)
    if (10 < event.x < 360) and (10 < event.y < 210):
        draw_color_circle(event)
        return
    messagebox.showwarning("Warning", "Mouse pointer is not in the rectangle")
    pass


def draw_color_circle(event):
    my_color = ["Blue", "Green", "Red", "Purple", "Yellow"]
    #print(f"x is {event.x}, y is {event.y}")
    rand_color = random.choice(my_color)
    x0 = event.x
    y0 = event.y
    x1 = x0 + 10
    y1 = y0 + 10
    my_canvas.create_oval(x0, y0, x1, y1, fill=rand_color)

root = tk.Tk()


my_canvas = tk.Canvas(root, bg='yellow', height=350, width=500)
my_canvas.pack()

my_canvas.bind('<ButtonPress-1>', mouse_outside_scream)
#my_canvas.bind('<ButtonPress-1>', draw_color_circle)

root.mainloop()