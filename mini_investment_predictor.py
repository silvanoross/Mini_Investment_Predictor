# ------------------------------------------------------------------------ #
# Title: mini_investment_predictor GUI for MIP
# Description: Use tkinter to create a gui for user to input investment values
# ChangeLog (Who,When,What):
# SRoss 07/06/2022 Script Begin
# SRoss 07/07/2022 created window with title
# ------------------------------------------------------------------------ #


import tkinter as tk
from tkinter import ttk as ttk
from tkinter import *
import fire
# Create root node object
mip_window = tk.Tk()
mip_window.geometry("800x200")  # define size of the window
mip_window.title("Mini Investment Predictor")

# Create label
# lbl_title_mip = ttk.Label(mip_window, text="Please Enter Values")
# lbl_title_mip.grid()

# String Variables for MIP
initial_var = tk.IntVar()
interest_var = tk.IntVar()
years_var = tk.IntVar()
compound_var = tk.IntVar()


# Function for calculation in MIP
def calculate():
    """
    performs simple equation FV = PV*(1+(i/n))^nt
    :return: Final Investment Value
    """
    # initial = initial_var.get()
    # interest = interest_var.get()
    # years = years_var.get()
    # compound = compound_var.get()
    try:
        if compound_var.get() > 0:
            final_value = initial_var.get() * (1 + ((interest_var.get() / 100) / compound_var.get())) ** (
                    years_var.get() * compound_var.get())
            # convert to string values
            disp_text.config(
                text=f"After {years_var.get()} years your portfolio will be worth ${final_value: .2f}")
        else:
            print("A value of 0 was entered somewhere, try to run this again")
    except Exception as e:
        print("Compound rate cannot be zero")
        print(e, e.__doc__, type(e), sep='\n')
        final_value = e
    return final_value


# Create initial label & entry
initial_lbl = ttk.Label(mip_window, text="Initial Investment")
initial_entry = ttk.Entry(mip_window, textvariable=initial_var)

# Create interest label & entry
interest_lbl = ttk.Label(mip_window, text="Interest Rate %")
interest_entry = ttk.Entry(mip_window, textvariable=interest_var)

# Create years label & entry
years_lbl = ttk.Label(mip_window, text="Number of Years")
years_entry = ttk.Entry(mip_window, textvariable=years_var)

# Create compound label & entry
compound_lbl = ttk.Label(mip_window, text="Compounds/Year")
compound_entry = ttk.Entry(mip_window, textvariable=compound_var)

# Create Calculate Button
calc_btn = tk.Button(mip_window, text='Calculate', command=calculate)

# # Display label for final value
disp_text = tk.Label(mip_window, font='Helvetica')

# format with grid
initial_lbl.grid(row=0, column=0)
initial_entry.grid(row=0, column=1)
interest_lbl.grid(row=1, column=0)
interest_entry.grid(row=1, column=1)
years_lbl.grid(row=2, column=0)
years_entry.grid(row=2, column=1)
compound_lbl.grid(row=3, column=0)
compound_entry.grid(row=3, column=1)
calc_btn.grid(row=4, column=1)
disp_text.grid(row=5, column=1)

mip_window_run = mip_window.mainloop()

if __name__ == '__main__':
    fire.Fire(mip_window_run)
