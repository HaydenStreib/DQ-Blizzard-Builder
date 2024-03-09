#Hayden Streib
#3/6/2024
#Final Project Blizzard Builder
import tkinter as tk
from tkinter import messagebox

def start_menu(root, logo):
    start_window = root
    start_window.title("DQ Blizzard Builder")
    start_image_label = tk.Label(start_window, image=logo)
    start_image_label.pack()
    start_label = tk.Label(start_window, text = "Welcome to the Dairy Queen Blizzard Builder")
    start_label.pack()
    start_button = tk.Button(start_window, text = "Start", command = lambda: select_size(root))
    start_button.pack()
    exit_button = tk.Button(start_window, text = "Exit", command = exit)
    exit_button.pack()

def select_size(root):
    size_window = tk.Toplevel(root)
    size_window.title("Select Your Blizzard Size")
    size_label = tk.Label(size_window, text = "pick your size")
    size_label.pack()
    size_var = tk.StringVar()
    small_btn = tk.Radiobutton(size_window, text = "Small", variable = size_var, value = "Small")
    small_btn.pack()
    medium_btn = tk.Radiobutton(size_window, text = "Medium", variable = size_var, value = "Medium")
    medium_btn.pack()
    large_btn = tk.Radiobutton(size_window, text = "Large", variable = size_var, value = "Large")
    large_btn.pack()
    next_button = tk.Button(size_window, text = "Next", command = lambda: check_size(root, size_window, size_var))
    next_button.pack()
    exit_button = tk.Button(size_window, text = "Exit", command = exit)
    exit_button.pack()
    size_window.grab_set()

def check_size(root, size_window, size_var):
    selected_size = size_var.get()
    if selected_size == "":
        messagebox.showwarning("Size not selected", "Please select size", parent=size_window)
    else:
        blizzard["size"] = selected_size
        size_window.destroy()
        select_flavor(root)

def select_flavor(root):
    flavor_window = tk.Toplevel(root)
    flavor_window.title("Select Your Soft Serve Flavor")
    flavor_label = tk.Label(flavor_window, text = "Choose Your Soft Serve Flavor")
    flavor_label.pack()
    flavor_var = tk.StringVar()
    chocolate_btn = tk.Radiobutton(flavor_window, text = "chocolate", variable = flavor_var, value = "chocolate")
    chocolate_btn.pack()
    vanilla_btn = tk.Radiobutton(flavor_window, text = "vanilla", variable = flavor_var, value = "vanilla")
    vanilla_btn.pack()
    next_button = tk.Button(flavor_window, text = "Next", command = lambda: check_flavor(root, flavor_window, flavor_var))
    next_button.pack()
    exit_button = tk.Button(flavor_window, text = "Exit", command = exit)
    exit_button.pack()
    flavor_window.grab_set()

def check_flavor(root, flavor_window, flavor_var):
    selected_flavor = flavor_var.get()
    if selected_flavor == "":
        messagebox.showwarning("Flavor not selected", "Please select flavor", parent=flavor_window)
    else:
        blizzard["flavor"] = selected_flavor
        flavor_window.destroy()
        select_toppings(root)

def topping_selection(event):
    toppings_listbox = event.widget
    selected_toppings = toppings_listbox.curselection()
    blizzard["toppings"] = [toppings_listbox.get(i) for i in selected_toppings]
    
def select_toppings(root):
    toppings_window = tk.Toplevel(root)
    toppings_window.title("Select your Blizzard Toppings")
    toppings_label = tk.Label(toppings_window, text = "Pick your Toppings")
    toppings_label.pack()
    toppings_listbox = tk.Listbox(toppings_window, selectmode=tk.MULTIPLE)
    toppings_listbox.insert(tk.END, "oreo")
    toppings_listbox.insert(tk.END, "reeces")
    toppings_listbox.insert(tk.END, "snickers")
    toppings_listbox.insert(tk.END, "strawberry")
    toppings_listbox.insert(tk.END, "hot fudge")
    toppings_listbox.insert(tk.END, "heath bar")
    toppings_listbox.insert(tk.END, "butter finger")
    toppings_listbox.insert(tk.END, "cookie dough")
    toppings_listbox.insert(tk.END, "brownie bites")
    toppings_listbox.insert(tk.END, "chocolate chunks")
    toppings_listbox.insert(tk.END, "cheese cake")
    toppings_listbox.bind("<<ListboxSelect>>", topping_selection)
    toppings_listbox.pack()
    next_button = tk.Button(toppings_window, text = "Next", command = lambda: check_toppings(root, toppings_window))
    next_button.pack()
    exit_button = tk.Button(toppings_window, text = "Exit", command = exit)
    exit_button.pack()
    toppings_window.grab_set()

def check_toppings(root, toppings_window):
    selected_toppings = blizzard["toppings"]
    if not selected_toppings:
        messagebox.showwarning("Toppings not selected", "Please select toppings", parent=toppings_window)
    else:
        toppings_window.destroy()
        show_order(root)

def show_order(root):
    order_window = tk.Toplevel(root)
    order_window.title("Your completed Blizzard")
    order_text = "Size: " + blizzard["size"] + "\n" \
        + "Flavor: " + blizzard["flavor"] + "\n" \
        + "Toppings: " + ", ".join(blizzard["toppings"])
    order_msg = tk.Message(order_window, text=order_text, width=200)
    order_msg.pack()
    exit_button = tk.Button(order_window, text = "Exit", command = exit)
    exit_button.pack()
    order_window.grab_set()
    
root = tk.Tk()
start_image = tk.PhotoImage(file="dqlogo.png")
blizzard = {}
start_menu(root, start_image)
root.mainloop()
