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

