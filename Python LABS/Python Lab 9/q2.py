import tkinter as tk
from tkinter import messagebox

def convert_d_to_b(entrybar):
    input_money = float(entrybar.get())
    output_money = input_money * 30
    output_str = "{:.2f}".format(input_money) + " USD = " + "{:.2f}".format(output_money) + " THB"
    messagebox.showinfo("USD -> THB", output_str)
    print(output_str)

def convert_b_to_d(entrybar):
    input_money = float(entrybar.get())
    output_money = input_money / 30
    output_str = "{:.2f}".format(input_money) + " THB = " + "{:.2f}".format(output_money) + " USD"
    messagebox.showinfo("THB -> USD", output_str)
    print(output_str)


root = tk.Tk()

usd_to_thb = tk.Button(root, text="USD -> THB", command=lambda: convert_d_to_b(money_in))
usd_to_thb.place(relx=0, rely=0.3333, relwidth=0.9, relheight=0.25)

thb_to_usd = tk.Button(root, text="THB -> USD", command=lambda: convert_b_to_d(money_in))
thb_to_usd.place(relx=0, rely=0.6666, relwidth=0.9, relheight=0.25)

money_in = tk.Entry(root)
money_in.place(relx=0, rely=0, relwidth=0.9, relheight=0.25)

root.mainloop()

