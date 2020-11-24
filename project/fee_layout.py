from tkinter import *   
from tkinter import ttk
import mysql.connector

def run():
    #Connecting to database:
    mydb = mysql.connector.connect(user='root', password='passwor0', host='localhost', database="project")
    my_cursor = mydb.cursor()

    #Creating the root window:
    root = Tk()
    root.minsize(550,550)
    root.maxsize(550,550)
    root.title("Fee Structure")
    root.iconbitmap("favicon.ico")
    root.config(bg="#161616")


    #Creating label:
    label = Label(root, text="Fee Structure 2020-2021", font=("Cambria",20,UNDERLINE), bg="#161616", fg="white")
    label.place(relx=0.5,rely=0.1,anchor=CENTER)

    #Making the table layout:
    my_tree = ttk.Treeview(root, columns=(1,2,3), show="headings", height="15")
    my_tree.place(relx=0.5,rely=0.7, anchor=CENTER)

    #Creating the heading of the table:
    my_tree.heading(1, text="Class")
    my_tree.heading(2, text="Annual Fee")
    my_tree.heading(3, text="Tution Fee")
    #Making heading--> columns:
    my_tree.column(1,  width=160, anchor=CENTER)
    my_tree.column(2,  width=160, anchor=CENTER)
    my_tree.column(3,  width=160, anchor=CENTER)


    #Styling tabel:
    style = ttk.Style(root)

    # Setting ttk theme to "clam" as to give some bump to the headings and to make the table look dark like our theme:
    style.theme_use("clam")
    style.configure("Treeview", font = ("Times", 12, "bold"), background="#161616", foreground="white", rowheight=25, fieldbackground="161616")
    style.configure("Treeview.Heading", font = ("Arial", 10), background="#161616", foreground="white", fieldbackground="161616")
    
    #Change selected color:
    style.map("Treeview", background=[('selected', 'black')])
    style.map("Treeview.Heading", background=[('selected', 'black')])

    #Querying data:
    query = "Select * from fee_structure"
    my_cursor.execute(query)
    rows= my_cursor.fetchall()

    #fetching and inserting in the values from a for loop:
    for i in rows:
        my_tree.insert('', 'end', values=i)

    #Creating a back button:
    back_btn = Button(root, text="BACK",padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white", command=root.destroy)
    back_btn.place(relx=0.9, rely=0.97, anchor=S)

    mydb.close()
    root.mainloop()