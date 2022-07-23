"""
location, price, size, (title)
View all, search by name, location or parameters
"""

import tkinter as tk
import backend
import webscraper

def box_view():
    listBox.delete(0,tk.END)
    for row in backend.viewAll():
        listBox.insert(tk.END, row)

def box_search():
    listBox.delete(0,tk.END)
    for row in backend.search(e1.get()):
        listBox.insert(tk.END, row)

def box_filter():
    listBox.delete(0,tk.END)
    for row in backend.filter(e2.get(),e3.get()):
        listBox.insert(tk.END, row)

root = tk.Tk()

backend.conn(webscraper.scrape())

l1 = tk.Label(root, text="Search by locality")
l1.grid(row=0, column=0)

searchBy = tk.StringVar()
e1 = tk.Entry(root, textvariable=searchBy, width=10)
e1.grid(row=0, column=1)

b1 = tk.Button(root, text="Search",command=box_search)
b1.grid(row=0, column=2)

b2 = tk.Button(root, text="View All", command=box_view)
b2.grid(row=0, column=3)

b3 = tk.Button(root, text="X")
b3.grid(row=0, column=4)

l2 = tk.Label(root, text="Min price")
l2.grid(row=1, column=0)

minPrice = tk.StringVar()
e2 = tk.Entry(root, textvariable=minPrice, width=5)
e2.grid(row=1, column=1)

l3 = tk.Label(root, text="Max price")
l3.grid(row=1, column=2)

maxPrice = tk.StringVar()
e3 = tk.Entry(root, textvariable=maxPrice, width=5)
e3.grid(row=1, column=3)

b4 = tk.Button(root, text="Filter",command=box_filter)
b4.grid(row=1, column=4)

listBox = tk.Listbox(root, height=6, width=45)
listBox.grid(row=2, column=0, rowspan=5, columnspan=6)

scrollBar = tk.Scrollbar(root)
scrollBar.grid(row=2, column=5, columnspan=2)

listBox.configure(yscrollcommand=scrollBar.set)
scrollBar.configure(command=listBox.yview)

root.mainloop()
