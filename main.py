from produkts import Item
import tkinter as tk
from tkinter import ttk, END
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("inventars")
root.geometry("350x600")

items_list = []
total_sales_value = 0.0  # Variable to hold total sales value

# Frame setup
frame = ttk.Frame(root)
frame.grid(padx=10, pady=10)

options = {'padx': 5, 'pady': 5}

# Labels
title_label = ttk.Label(frame, text='Title')
title_label.grid(column=0, row=0, sticky='E', **options)

category_label = ttk.Label(frame, text='Category')
category_label.grid(column=0, row=1, sticky='E', **options)

quantity_label = ttk.Label(frame, text='Quantity')
quantity_label.grid(column=0, row=2, sticky='E', **options)

price_label = ttk.Label(frame, text='Price')
price_label.grid(column=0, row=3, sticky='E', **options)

# Entry fields
title = tk.StringVar()
title_entry = ttk.Entry(frame, textvariable=title)
title_entry.grid(column=1, row=0, **options)

category = tk.StringVar()
category_entry = ttk.Entry(frame, textvariable=category)
category_entry.grid(column=1, row=1, **options)

quantity = tk.IntVar()
quantity_entry = ttk.Entry(frame, textvariable=quantity)
quantity_entry.grid(column=1, row=2, **options)

price = tk.DoubleVar()
price_entry = ttk.Entry(frame, textvariable=price)
price_entry.grid(column=1, row=3, **options)

# Refresh item list
def refresh_list():
    listbox.delete(0, END)
    for idx, item in enumerate(items_list, start=1):
        listbox.insert("end", f"{idx}. {item.title}, {item.category}, {item.quantity}, {item.price}€")

# Add item button function
def add_item_button_clicked():
    item_title = title.get()
    item_category = category.get()
    item_quantity = quantity.get()
    item_price = price.get()

    items_list.append(Item(item_title, item_category, item_quantity, item_price))
    result_label.config(text=items_list[-1].show_info())
    refresh_list()

    # Clear input fields
    title_entry.delete(0, END)
    category_entry.delete(0, END)
    quantity_entry.delete(0, END)
    price_entry.delete(0, END)


add_button = ttk.Button(frame, text='pievienot')
add_button.grid(column=2, row=0, sticky='W', **options)
add_button.configure(command=add_item_button_clicked)


listbox_title = ttk.Label(frame, text='saraksts')
listbox_title.grid(row=4, columnspan=3, **options)

listbox_frame = ttk.Frame(frame)
listbox_frame.grid(row=5, columnspan=3, **options)

listbox = tk.Listbox(listbox_frame, height=6, width=50, selectmode=tk.EXTENDED)
listbox.grid(row=0, column=0, sticky='nsew')


listbox_scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=listbox.yview)
listbox_scrollbar.grid(row=0, column=1, sticky='ns')

listbox.configure(yscrollcommand=listbox_scrollbar.set)


sold_items_title = ttk.Label(frame, text='pardotas lietas')
sold_items_title.grid(row=6, columnspan=3, **options)

sold_items_listbox_frame = ttk.Frame(frame)
sold_items_listbox_frame.grid(row=7, columnspan=3, **options)

sold_items_listbox = tk.Listbox(sold_items_listbox_frame, height=6, width=30, selectmode=tk.SINGLE)
sold_items_listbox.grid(row=0, column=0, sticky='nsew')


sold_items_listbox_scrollbar = ttk.Scrollbar(sold_items_listbox_frame, orient=tk.VERTICAL, command=sold_items_listbox.yview)
sold_items_listbox_scrollbar.grid(row=0, column=1, sticky='ns')

sold_items_listbox.configure(yscrollcommand=sold_items_listbox_scrollbar.set)


total_sales_title = ttk.Label(frame, text='visa summa')
total_sales_title.grid(row=8, columnspan=3, **options)

total_sales_listbox = tk.Listbox(frame, height=1, width=30, selectmode=tk.SINGLE)
total_sales_listbox.grid(row=9, columnspan=3, **options)


def edit_item():
    selected = listbox.curselection()

    if selected:
        selected_item = selected[0]
        item = items_list[selected_item]

        
        new_title = title.get() if title.get() else item.title
        new_category = category.get() if category.get() else item.category
        new_quantity = item.quantity
        if quantity_entry.get():
            try:
                new_quantity = int(quantity_entry.get())
            except ValueError:
                showinfo("ievadiet nummuru")
                return

        new_price = item.price
        if price_entry.get():
            try:
                new_price = float(price_entry.get())
            except ValueError:
                showinfo("ievadiet normalu cenu")
                return

        
        item.title = new_title
        item.category = new_category
        item.quantity = new_quantity
        item.price = new_price

        
        listbox.delete(selected_item)
        listbox.insert(selected_item, f"{new_title}, {new_category}, {new_quantity}, {new_price}€")

        
        title_entry.delete(0, END)
        category_entry.delete(0, END)
        quantity_entry.delete(0, END)
        price_entry.delete(0, END)


edit_button = ttk.Button(frame, text='rediget')
edit_button.grid(column=2, row=1, sticky='W', **options)
edit_button.configure(command=edit_item)


def sell_item():
    global total_sales_value
    new_text = ""
    for selected in listbox.curselection():
        item = items_list[selected]

        
        if item.quantity <= 0:
            showinfo("kluda", f"{item.title} izpardota")
            continue  

       
        total_sales_value += item.price

        
        sold_items_listbox.insert(END, f"{item.title}, {item.price}€")

        
        total_sales_listbox.delete(0, END)
        total_sales_listbox.insert(END, f"{total_sales_value}€")

        item.sell_item()
        new_text += item.show_info() + "\n"

    result_label.config(text=new_text)
    refresh_list()


sell_button = ttk.Button(frame, text='pardot')
sell_button.grid(column=2, row=2, sticky='W', **options)
sell_button.configure(command=sell_item)


result_label = ttk.Label(frame, text='')
result_label.grid(columnspan=3, **options)

root.mainloop()
