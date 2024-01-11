# ========================Importing the libraries========================
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
Root = Tk()
Root.title('Vending machine')

# ========================Global Variables==============================
user_input = ''
# list of items chosen by the user to buy
selected_items = {}

# ========================List=========================================

items = {
    "1": {"name": "Candy", "price": "2.00", "stock": random.randint(0, 10)},
    "2": {"name": "Chips", "price": "1.25", "stock": random.randint(0, 10)},
    "3": {"name": "Cold coffee", "price": "5.00", "stock": random.randint(0, 10)},
    "4": {"name": "Water", "price": "2.00", "stock": random.randint(0, 10)},
    "5": {"name": "Juice", "price": "3.00", "stock": random.randint(0, 10)},
    "6": {"name": "Chocolate", "price": "2.50", "stock": random.randint(0, 10)},
    "7": {"name": "Gummy bears", "price": "5.00", "stock": random.randint(0, 10)},
    "8": {"name": "Soda", "price": "3.00", "stock": random.randint(0, 10)},
    "9": {"name": "Muffin", "price": "4.00", "stock": random.randint(0, 10)},
    "10": {"name": "Biscuits", "price": "7.00", "stock": random.randint(0, 10)},
}


# ========================Functions=====================================

#function to show the items on the vending machine
def addToItemsList(txtarea, items):
    for key, item in items.items():
        txtarea.insert(tk.END, f"{key}, {item['name']} - ${item['price']} | {item['stock']}\n")


#function to store the input from the user thats used to select an item
def store_user_input():
    global user_input
    user_input = UserItemSelection.get()
    stored_variable.set(user_input)

#function to store the balance/money entered by the user
def store_balance():
    global balance
    balance_str = UserMoneyEntry.get()
    balance_str.strip()
    balance = float(balance_str)
    stored_variable.set(balance)

#function to print the selected item in the text area to tell them what they are buying and how much it costs
def print_selection_in_txtarea2(txtarea, items):
    global selected_items
    #selected_items = None
    if user_input in items:
        new_item = items[user_input]
        new_key = str(len(selected_items) + 1)
        new_item['key'] = str(max(int(key) for key in items.keys()) + 1)
        selected_items[new_key] = items[user_input]
        if selected_items[new_key]['stock'] > 0:
            txtarea.insert(tk.END, f"you have selected {selected_items[new_key]['name']} \ncosting ${selected_items[new_key]['price']}.\n")
            print(selected_items)
        else:
            txtarea.insert(tk.END, f"Sorry {selected_items[new_key]['name']} is out of stock\n")
    else:
        messagebox.showerror("Item Doesnt Exist", "Please select an item from the list.")


#function to proceed to checkout if the user has inserted enough money to pay for the items he will receive them and the change
#if not then he will be prompted to insert more money and that he has insufficient funds
def proceed_to_checkout():
    global balance, selected_items
    total_price = sum(float(item['price']) for item in selected_items.values())
    balance = float(balance)
    print(total_price)
    print(selected_items)
    print(balance)

    if balance >= total_price:
       change = balance - total_price
       balance = change
       print(change)
       #print a messagebox show info with the name of every item in the selected_items
       item_names = '\n'.join(item['name'] for item in selected_items.values())
       Reset(False)
       messagebox.showinfo("Checkout Successful", f"Thank you for shopping!\nDispensed items:\n{item_names}\nChange: ${change:.2f}")
       #messagebox.showinfo("Checkout Successful",f"Thank you for shopping!\nDispensed item: {selected_items["0"]['name']}\nChange: ${change:.2f}")
    else: messagebox.showerror("Insufficient Funds", "Insufficient funds. Please insert more money.")

#function to reset everything
def Reset(resetMoneyEntry = True):
    global user_input, balance, selected_items
    user_input = ''
    selected_items = None
    UserItemSelection.delete(0, END)
    if resetMoneyEntry:
        balance = 0.0
        UserMoneyEntry.delete(0, END)
    else:
        UserMoneyEntry.delete(0, END)
        UserMoneyEntry.insert(tk.END,balance)

    PromptArea.delete(1.0, END)


# ========================Designing the interface========================

#the title of the vending machine
Root = Label(Root, text='Vending machine', font='arial 18 bold', width=60, bg='purple', bd=10, fg='white',
             relief=RAISED)
Root.grid(row=0, column=0, padx=10, pady=10)

#the frame that covers everything
F1 = Frame(relief=RAISED, bd=20, bg='purple')
F1.grid(row=1, column=0, padx=10, pady=10)

#the frame thats on the left side and only covers the user inputs/prompts leaving the items list outside
F2 = Frame(F1, relief=RAISED, bd=10, bg='purple')
F2.grid(row=1, column=0, padx=10, pady=10)

#title of the input thats used to select the items
ItemSelectTitle = Label(F2, text='Enter the number for product', bg='purple', fg='white', width=30, font='arial 15 bold')
ItemSelectTitle.grid(row=1, column=0)

#title of the input thats used to insert money
MoneyInsertTitle = Label(F2, text='Insert money', bg='purple', fg='white', width=30, font='arial 15 bold')
MoneyInsertTitle.grid(row=5, column=0)

#item selection textbox/Entry that allows the user to select an item
UserItemSelection = Entry(F2, width=18, bd=7, font='arial 15 bold', justify='center')
UserItemSelection.grid(row=2, column=0, padx=10, pady=10)

#money entry textbox/Entry that allows the user to insert money
UserMoneyEntry = Entry(F2, width=18, bd=7, font='arial 15 bold', justify='center')
UserMoneyEntry.grid(row=6, column=0, padx=10, pady=10)

#side panel that shows the items that the user can buy
ItemsList = Text(F1, width=24, height=22, bd=10, bg='grey', font='arial 13 bold', fg='white')
ItemsList.grid(row=1, column=1, padx=10, pady=10)

#PromptArea that prints the items that the user has selected and how much they cost
PromptArea = Text(F2, height=5, width=25, bd=7, font='arial 12 bold',bg='grey', fg='white')
PromptArea.grid(row=3, column=1, padx=10, pady=10)

# adding list to the grey box that i have created in the gui
addToItemsList(ItemsList, items)

stored_variable = StringVar()
# =======================Buttons==============================

#Button that the user uses to confirm an item they wanna select after they enter the number
ItemEnterBtn = Button(F2, width=18, text='Enter', font='arial 15 bold', bd=18, bg='lime', fg='white',
            command=lambda: (store_user_input(),  print_selection_in_txtarea2(PromptArea, items)))
ItemEnterBtn.grid(row=3, column=0, padx=25, pady=25)

#Button that the user uses to reset the vending machine
ResetBtn = Button(F2, width=15, text='Reset', font='arial 15 bold', bd=18, bg='white', fg='black',
            command=lambda: (UserItemSelection.delete(0, END), UserMoneyEntry.delete(0, END), PromptArea.delete(1.0, END)))
ResetBtn.grid(row=4, column=0, padx=25, pady=25)

#Button that the user uses to check out/confirm their purchase
CheckOutBtn = Button(F2, width=18, text='Proceed to checkout', font='arial 15 bold', bd=18, bg='white', fg='black',
            command=lambda: (store_balance(), (proceed_to_checkout())))
CheckOutBtn.grid(row=7, column=0, padx=25, pady=25)

Root.mainloop()