from tkinter import *
import mysql.connector
from tkinter import messagebox
import fee_layout
from PIL import ImageTk, Image


def fee_menu():
    #Creating the fee window:
    fee_menu_window = Toplevel()
    fee_menu_window.title("Fee Details")
    fee_menu_window.iconbitmap("favicon.ico")
    fee_menu_window.config(bg="#161616")
    fee_menu_window.minsize(600,600)
    fee_menu_window.maxsize(600,600)
    

    #Adding illustrations:
    img = Image.open("ques2.jpg")
    resize = img.resize((60, 60), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(resize)
    my_label = Label(fee_menu_window, image=my_img, border=0)
    my_label.place(relx=0.3, rely=0.8, anchor=CENTER)

    
    img2 = Image.open("ques3.jpg")
    resize2 = img2.resize((60, 60), Image.ANTIALIAS)
    my_img2 = ImageTk.PhotoImage(resize2)
    my_label2 = Label(fee_menu_window, image=my_img2, border=0)
    my_label2.place(relx=0.2, rely=0.2, anchor=CENTER)

    img3 = Image.open("ques6.jpg")
    resize3 = img3.resize((60, 60), Image.ANTIALIAS)
    my_img3 = ImageTk.PhotoImage(resize3)
    my_label3 = Label(fee_menu_window, image=my_img3, border=0)
    my_label3.place(relx=0.7, rely=0.5, anchor=CENTER)

    img4 = Image.open("ques5.jpg")
    resize4 = img4.resize((60, 60), Image.ANTIALIAS)
    my_img4 = ImageTk.PhotoImage(resize4)
    my_label4 = Label(fee_menu_window, image=my_img4, border=0)
    my_label4.place(relx=0.9, rely=0.2, anchor=CENTER)



    #Creating the display text:
    header = Label(fee_menu_window, text="Hii There!! What Do You Wanna To Do?", bg="#161616", fg="white", font=("Cambria",20))
    header.place(relx=0.5, rely=0.1, anchor=CENTER)

    #Creating buttons:
    fee_structure = Button(fee_menu_window, text="Fee-Structure", padx=5, pady=5, font='Ubuntu 15 bold', bg="#161616", fg="white", command=fee_layout.run)
    fee_structure.place(relx=0.5, rely=0.45, anchor=CENTER)

    upd_fee_structure = Button(fee_menu_window, text="Update-Structure", padx=5, pady=5, font='Ubuntu 15 bold', bg="#161616", fg="white", command=upd_fee_structuree)
    upd_fee_structure.place(relx=0.5, rely=0.6, anchor=CENTER)

    back_btn = Button(fee_menu_window, text="BACK",padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white", command=fee_menu_window.destroy)
    back_btn.place(relx=0.9, rely=0.97, anchor=S)


    fee_menu_window.mainloop()


def upd_fee_structuree():
    #Making entry and window global:
    global upd_fee_structure_window
    global upd_fee_structure_class_entry
    global upd_fee_structure_class_annual_entry
    global upd_fee_structure_tution_fee_entry
    #Connecting to the database:
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()

    #Creating window:
    upd_fee_structure_window = Toplevel()
    upd_fee_structure_window.title("Update Fee Structure")
    upd_fee_structure_window.iconbitmap("favicon.ico")
    upd_fee_structure_window.config(bg="#161616")
    upd_fee_structure_window.minsize(550,550)
    upd_fee_structure_window.maxsize(550,550)

    #Querying for data:
    my_cursor.execute("select * from fee_structure")
    mydb.close()

    #Creating a title or header:
    title_text = Label(upd_fee_structure_window, text="Update Fee Structure 2020-2021", font=("Cambria",20,UNDERLINE), bg="#161616", fg="white")
    title_text.place(relx=0.5, rely=0.1, anchor=CENTER)

    #Creating Labels:
    upd_fee_structure_class = Label(upd_fee_structure_window, text="Class:",  bg="#161616", fg="white", font=("Times",15,"bold"))
    upd_fee_structure_class.place(relx=0.5,rely=0.4, anchor=CENTER)

    upd_fee_structure_annual = Label(upd_fee_structure_window, text="Annual Charges:",  bg="#161616", fg="white", font=("Times",15,"bold"))
    upd_fee_structure_annual.place(relx=0.42,rely=0.5, anchor=CENTER)

    upd_fee_structure_tution_fee = Label(upd_fee_structure_window, text="Tution Fees:",  bg="#161616", fg="white", font=("Times",15,"bold"))
    upd_fee_structure_tution_fee.place(relx=0.45,rely=0.6, anchor=CENTER)

    #Creating Entry boxes:
    upd_fee_structure_class_entry = Entry(upd_fee_structure_window, width=10, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    upd_fee_structure_class_entry.place(relx=0.7, rely=0.4, anchor=E, height=30)

    upd_fee_structure_class_annual_entry = Entry(upd_fee_structure_window, width=10, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    upd_fee_structure_class_annual_entry.place(relx=0.7, rely=0.5, anchor=E, height=30)

    upd_fee_structure_tution_fee_entry = Entry(upd_fee_structure_window, width=10, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    upd_fee_structure_tution_fee_entry.place(relx=0.7, rely=0.6, anchor=E, height=30)

    #Creating update button:
    upd_fee_structure_update_btn = Button(upd_fee_structure_window, text="Update",padx=5, pady=5, font='Ubuntu 12 bold', bg="#161616", fg="white", command=upd_fee_annual_tution)
    upd_fee_structure_update_btn.place(relx=0.5, rely=0.75, anchor=CENTER)

    #Creating back button:
    back_btn = Button(upd_fee_structure_window, text="BACK",padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white", command=upd_fee_structure_window.destroy)
    back_btn.place(relx=0.9, rely=0.97, anchor=S)


def upd_fee_annual_tution():
    try:
        #Connecting to the database:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
        my_cursor = mydb.cursor()

        #Query for updating a fee strucutre:
        my_cursor.execute(f"update fee_structure set Annual_Charges={upd_fee_structure_class_annual_entry.get()} where Class='{upd_fee_structure_class_entry.get()}'")
        my_cursor.execute(f"update fee_structure set  Tution_Fee={upd_fee_structure_tution_fee_entry.get()} where Class='{upd_fee_structure_class_entry.get()}'")
        def pop_fee_structure_update_mssg():
            messagebox.showinfo("Status", "UPDATED!")  
        pop_fee_structure_update_mssg()
        mydb.commit()
        mydb.close()

        #Clear the text box:
        upd_fee_structure_class_entry.delete(0,END)
        upd_fee_structure_tution_fee_entry.delete(0,END)
        upd_fee_structure_class_annual_entry.delete(0, END)
    except:
        #Creating a lil popup mssg:
        def popup13():
            messagebox.showerror("Status", "Class don't exists/Entries not filled")  
        popup13() 
