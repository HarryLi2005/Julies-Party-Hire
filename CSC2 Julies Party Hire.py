# import tkinter so we can make a GUI
from tkinter import *


def quit():
    main_window.destroy()

# print details


def print_hire_details():
    # these are the global variables that are used
    global j_names, total_entries, name_count
    name_count = 0
    # Create the column headings
    Label(main_window, font=("Helvetica 10 bold"),
          text="Receipt Number").grid(column=0, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Customer Name").grid(column=1, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Item").grid(column=2, row=7)
    Label(main_window, font=("Helvetica 10 bold"),
          text="Amount of items").grid(column=3, row=7)


# add each item in the list into its own row
    while name_count < total_entries:
        Label(main_window, text=name_count).grid(column=0, row=name_count+8)
        Label(main_window, text=(hire_details[name_count][0])).grid(
            column=1, row=name_count+8)
        Label(main_window, text=(hire_details[name_count][1])).grid(
            column=2, row=name_count+8)
        Label(main_window, text=(hire_details[name_count][2])).grid(
            column=3, row=name_count+8)
        name_count += 1


# Check the inputs are all valid


def check_inputs():
    # these are the global variables that are used
    global hire_details, name, item, amount_item, total_entries
    input_check = 0
    Label(main_window, text="               ") .grid(column=2, row=0)
    Label(main_window, text="               ") .grid(column=2, row=1)
    Label(main_window, text="               ") .grid(column=2, row=2)
    Label(main_window, text="               ") .grid(column=2, row=3)
    if len(name.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=0)
        input_check = 1
    if len(item.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=1)
        input_check = 1
    if (amount_item.get().isdigit()):
        if int(amount_item.get()) < 1 or int(amount_item.get()) > 500:
            Label(main_window, fg="red", text="1-500 only") .grid(column=2, row=2)
            input_check = 1
    else:
        Label(main_window, fg="red", text="1-500 only") .grid(column=2, row=2)
        input_check = 1
    if input_check == 0:
        append_name()

def append_name():
    # these are the global variables that are used
    global hire_details, name, item, amount_item, total_entries
    # append each item to its own area of the list
    hire_details.append([name.get(), item.get(),
                         amount_item.get()])
    # clear the boxes
    name.delete(0, 'end')
    item.delete(0, 'end')
    amount_item.delete(0, 'end')
    total_entries += 1


def delete_row():
    # these are the global variables that are used
    global hire_details, delete_item, total_entries, name_count
    # find which row is to be deleted and delete it
    del hire_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0, 'end')
    # clear the last item displayed on the GUI
    Label(main_window, text="                         ").grid(column=0, row=name_count+7)
    Label(main_window, text="                         ").grid(column=1, row=name_count+7)
    Label(main_window, text="                         ").grid(column=2, row=name_count+7)
    Label(main_window, text="                         ").grid(column=3, row=name_count+7)
    Label(main_window, text="                         ").grid(column=4, row=name_count+7)
    # print all the items in the list
    print_hire_details()


def setup_buttons():
    # these are the global variables that are used
    global hire_details, name, item, amount_item, total_entries, delete_item
    # create all the empty and default labels, buttons and entry boxes. Put them in the correct grid location
    Label(main_window, text="Customer Name") .grid(column=0, row=0, sticky=E)
    name = Entry(main_window)
    name.grid(column=1, row=0)
    Label(main_window, text="Item") .grid(column=3, row=0, sticky=E)
    item = Entry(main_window)
    item.grid(column=4, row=0)
    Button(main_window, text="Quit", command=quit,
           width=10) .grid(column=8, row=0, sticky=E)
    Button(main_window, text="Append Details",
           command=check_inputs) .grid(column=8, row=1)
    Button(main_window, text="Print Details", command=print_hire_details,
           width=10) .grid(column=8, row=2, sticky=E)
    Label(main_window, text="Amounts of item") .grid(column=5, row=0, sticky=E)
    amount_item = Entry(main_window)
    amount_item.grid(column=6, row=0)
    Label(main_window, text="Receipt #") .grid(column=6, row=4, sticky=E)
    delete_item = Entry(main_window)
    delete_item .grid(column=7, row=4)
    Button(main_window, text="Delete Row", command=delete_row,
           width=10) .grid(column=8, row=4, sticky=E)
    Label(main_window, text="               ") .grid(column=2, row=0)


def main():
    # these are the global variables that are used
    global main_window
    global hire_details, total_entries
    hire_details = []
    total_entries = 0
    # create the GUI and start it up
    main_window = Tk()
    setup_buttons()
    main_window.mainloop()


main()