from tkinter import *
from tkinter import messagebox
from tkinter import ttk, filedialog
import numpy
import pandas as pd

root = Tk()
root.title("Excel Datasheet Viewer")
root.geometry("1100x400+200+200")


# root.configure(bg="black")

def Open():
    filename = filedialog.askopenfilename(title="open a File",
                                          filetypes=(("xlsx files", ".*xlsx"), ("All Files", "*.")))

    if filename:
        try:
            filename = r"{}".format(filename)
            df = pd.read_excel(filename)
        except:
            messagebox.showerror("Error 404 found")

    #now we have to clear previous data to enter new data
    tree.delete(*tree.get_children())

    #datasheet headings
    tree['column']=list(df.columns)
    tree['show']="headings"

    #heading title
    for col in tree['columns']:
        tree.heading(col,text=col)

    #enter data
    df_rows=df.to_numpy().tolist()
    for row in df_rows:
        tree.insert("","end",values=row)


# #icon images
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

# frame
frame = Frame(root)
frame.pack(pady=25)

# Treeview
tree = ttk.Treeview(frame)
tree.pack()

# button
button = Button(root, text="Open", width=60, height=2, font=30, fg="white", bg="#0078d7", command=Open)
button.pack(padx=10, pady=20)

root.mainloop()
