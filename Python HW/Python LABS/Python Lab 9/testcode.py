from tkinter import *

def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return

def leave(event):
    print('Mouse has left the widget')

master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you doit.\n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind('<Motion>', motion)
msg.bind('<Leave>', leave)
msg.pack()
mainloop()