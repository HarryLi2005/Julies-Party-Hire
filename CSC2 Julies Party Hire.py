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
