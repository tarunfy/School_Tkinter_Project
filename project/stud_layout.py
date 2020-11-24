from tkinter import *   
from tkinter import ttk
import mysql.connector

def run():
    #Connecting to database:
    mydb = mysql.connector.connect(user='root', password='passwor0', host='localhost', database="project")
    my_cursor = mydb.cursor()

    #making the window:
    root = Tk()
    root.minsize(650,550)
    root.maxsize(650,550)
    root.title("Students")
    root.iconbitmap("favicon.ico")
    root.config(bg="#161616")


    #Creating label:
    label = Label(root, text="List Of All The Students", font=("Cambria",20,UNDERLINE), bg="#161616", fg="white")
    label.place(relx=0.5,rely=0.1,anchor=CENTER)

    #Creating the table layout:
    my_tree = ttk.Treeview(root, columns=(1,2,3,4,5,6,7,8,9), show="headings", height="15")
    my_tree.place(relx=0.5,rely=0.7, anchor=CENTER)

    #Creating the heading of the table:
    my_tree.heading(1, text="ID")
    my_tree.heading(2, text="Session")
    my_tree.heading(3, text="Name")
    my_tree.heading(4, text="Class")
    my_tree.heading(5, text="Section")
    my_tree.heading(6, text="Roll Num")
    my_tree.heading(7, text="Sub 1")
    my_tree.heading(8, text="Sub 2")
    my_tree.heading(9, text="Sub 3")
    
    #Making heading--> columns:
    my_tree.column(1,  width=50, anchor=CENTER)
    my_tree.column(2,  width=70, anchor=CENTER)
    my_tree.column(3,  width=70, anchor=CENTER)
    my_tree.column(4,  width=70, anchor=CENTER)
    my_tree.column(5,  width=70, anchor=CENTER)
    my_tree.column(6,  width=70, anchor=CENTER)
    my_tree.column(7,  width=70, anchor=CENTER)
    my_tree.column(8,  width=70, anchor=CENTER)
    my_tree.column(9,  width=70, anchor=CENTER)


    #Styling tabel:
    style = ttk.Style(root)
    # Setting ttk theme to "clam" as to give some bump to the headings and to make the table look dark like our theme:
    style.theme_use("clam")
    style.configure("Treeview", font = ("Times", 12, "bold"), background="#161616", foreground="white", rowheight=25, fieldbackground="161616")
    style.configure("Treeview.Heading", font = ("Arial", 10), background="#161616", foreground="white", fieldbackground="161616")
    #Change selected color:
    style.map("Treeview", background=[('selected', 'black')])
    style.map("Treeview.Heading", background=[('selected', 'black')])

    #Querying for data:
    query = "Select * from student1"
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
