# import tkinter so we can make a GUI
from tkinter import *

# quit subroutine


def quit():
    main_window.destroy()

# print details of all the camps


def print_camp_details():
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
        Label(main_window, text=(hire_details[name_count][3])).grid(
            column=4, row=name_count+8)
        name_count += 1


# Check the inputs are all valid


def check_inputs():
    # these are the global variables that are used
    global camp_details, name, item, amount_items, total_entries
    input_check = 0
    Label(main_window, text="               ") .grid(column=2, row=0)
    Label(main_window, text="               ") .grid(column=2, row=1)
    Label(main_window, text="               ") .grid(column=2, row=2)
    Label(main_window, text="               ") .grid(column=2, row=3)
    # Check that leader is not blank, set error text if blank
    if len(name.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=0)
        input_check = 1
    # Check that location is not blank, set error text if blank
    if len(item.get()) == 0:
        Label(main_window, fg="red", text="Required") .grid(column=2, row=1)
        input_check = 1
    # Check the number of campers is not blank and between 5 and 10, set error text if blank
    if (amount_items.get().isdigit()):
        if int(amount_items.get()) < 5 or int(amount_items.get()) > 10:
            Label(main_window, fg="red", text="5-10 only") .grid(column=2, row=2)
            input_check = 1
    else:
        Label(main_window, fg="red", text="5-10 only") .grid(column=2, row=2)
        input_check = 1
    # Check that weather is not blank, set error text if blank
    if input_check == 0:
        append_name()

