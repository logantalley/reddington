# Import libraries
import os
from tkinter import filedialog
from os import path
from tkinter import *
from tkinter import ttk

# Prepare the window
root = Tk()
root.title("Reddington")
root.iconbitmap("red.ico")
content = ttk.Frame(root, padding=(3,3,12,12))
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=75, height=75)
namelbl = ttk.Label(content, text="Tenant Code")
name = ttk.Entry(content)

# Define drop-down menus
FILETYPE = [
    "med",
    "rx",
    "eligibility"
]

YEAR = [
    "2018",
    "2019"
]

MONTH = [
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12"
]

type = StringVar()
type.set(FILETYPE[0])
ftype = OptionMenu(content, type, *FILETYPE)


month = StringVar()
month.set(MONTH[0])
mnth = OptionMenu(content, month, *MONTH)


year = StringVar()
year.set(YEAR[0])
yr = OptionMenu(content, year, *YEAR)

# Define the functions for the key buttons
class FileOperations:
    def open_file(self):
        self.file1 = filedialog.askopenfilename()

    def copy_file(self):
        dest = path.dirname(self.file1)
        os.rename(path.join(dest, self.file1), path.join(dest, name.get() + '_' + type.get() + '_' + year.get() + month.get() + '01.txt')) 

# Once we have this working in S3: this is the destination string:
# 'S3:/tpafiles/input/tenant/tpa/' + type.get() + '/' + year.get() + '/' + month.get().lstrip("0") + '/'

fileHandler = FileOperations()
# Define a table called 'cnames' which stands for client names
clientcodes = ('amtubg', 'kleenc', 'bucgrp')
clientnames = ('American Tubing', 'Kleenco Maintenance', 'Buchanan Group')
cnames = StringVar(value=clientnames)
# Define the key buttons
lbox = Listbox(content, listvariable=cnames, height=5)
grab = ttk.Button(content, text='Open File', command=fileHandler.open_file)
execute = ttk.Button(content, text='Execute', command=fileHandler.copy_file)

# Grid the content
content.grid(column=0, row=0, sticky=(N, S, E, W))
frame.grid(column=0, row=0, columnspan=1, rowspan=3, sticky=(N, S, E, W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=2)
name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=2, padx=2)
ftype.grid(column=0, row=0, sticky = W)
mnth.grid(column=0, row=1, sticky = W)
yr.grid(column=0, row=2, sticky = W)
grab.grid(column=3, row=2)
execute.grid(column=4, row=2)

root.mainloop()