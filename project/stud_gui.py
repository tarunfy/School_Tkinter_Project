from tkinter import *
import stud_layout
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk,Image

def Student_details():
    # Creating the window for student details menu:
    window_student = Toplevel()
    window_student.title("Student Details")
    window_student.iconbitmap("favicon.ico")
    window_student.config(bg="#161616")
    window_student.minsize(600,600)
    window_student.maxsize(600,600)

    #Inserting Image
    img_edit = Image.open("sd.jpg")
    resize = img_edit.resize((425,425),Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(resize)
    my_label = Label(window_student,image=my_img,border=0)
    my_label.place(relx=0.7, rely=0.45, anchor=CENTER)

    #Creating the display text:
    header = Label(window_student, text="Student Details", bg="#161616", fg="white", font=("Cambria",25,UNDERLINE))
    header.place(relx=0.28, rely=0.22, anchor=CENTER)
                    
    #Creating the buttons:
    button_new_stud = Button(window_student, text="Add Student",width=12,pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white", command=add_stud)
    button_new_stud.place(relx=0.2, rely=0.4, anchor=CENTER)

    button_display_details = Button(window_student, text="Show-Info",width=12,pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white", command=lambda: stud_layout.run())
    button_display_details.place(relx=0.2, rely=0.5, anchor=CENTER)

    button_find_student = Button(window_student, text="Find-Stud",width=12,pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white",  command=find_stud)
    button_find_student.place(relx=0.2, rely=0.6, anchor=CENTER)

    button_delete_student = Button(window_student, text="Del-Stud",width=12,pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white", command=del_stud)
    button_delete_student.place(relx=0.2, rely=0.7, anchor=CENTER)

    button_go_back= Button(window_student, text="BACK",width=12,pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white", command=window_student.destroy)
    button_go_back.place(relx=0.88, rely=0.97, anchor=S)

    window_student.mainloop()

#Creating submit function for data to be saved:
def submit():
    try:
        #Connecting to the database:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
        my_cursor = mydb.cursor()

        #Inserting into the table:
        my_cursor.execute(f"Insert into student1(ID,session,name,Class,section,roll_num,sub1,sub2,sub3) values({ID_entry.get()},'{session_entry.get()}','{name_entry.get()}',{Class_entry.get()},'{section_entry.get()}',{roll_num_entry.get()},'{sub1_entry.get()}','{sub2_entry.get()}','{sub3_entry.get()}')")
        mydb.commit()
        mydb.close()

        #Clear the text boxes:
        ID_entry.delete(0,END)
        session_entry.delete(0,END)
        name_entry.delete(0,END)
        Class_entry.delete(0,END)
        section_entry.delete(0,END)
        roll_num_entry.delete(0,END)
        sub1_entry.delete(0,END)
        sub2_entry.delete(0,END)
        sub3_entry.delete(0,END)   

        #Creating a lil popup mssg:
        def popup():
            messagebox.showinfo("Status", "Congrats!")  
        popup()  
    except:

        #Creating a lil popup mssg:
        def popup22():
            messagebox.showerror("Status", "ID already exists/Entries not filled")  
        popup22() 


def add_stud():
    #Making our entries variables global:
    global ID_entry
    global session_entry
    global name_entry
    global Class_entry
    global section_entry
    global roll_num_entry
    global sub1_entry
    global sub2_entry
    global sub3_entry
    
    #Creating the window for adding student details:
    new_stud_window = Toplevel()
    new_stud_window.title("Add Student Details")
    new_stud_window.iconbitmap("favicon.ico")
    new_stud_window.config(bg="#161616")
    new_stud_window.minsize(650,700)
    new_stud_window.maxsize(650,700)

    #Creating the display text:
    new_stud_header = Label(new_stud_window, text="ADD Student Details", bg="#161616", fg="white", font=("Cambria",20,"bold", UNDERLINE))
    new_stud_header.place(relx=0.5, rely=0.1, anchor=CENTER)

    #Creating the lables:
    ID = Label(new_stud_window, text="ID", bg="#161616", fg="white", font=("Times",15,"bold"))
    ID.place(relx=0.1, rely=0.2, anchor=W)

    session = Label(new_stud_window, text="Session", bg="#161616", fg="white", font=("Times",15,"bold"))
    session.place(relx=0.1, rely=0.27, anchor=W)

    name = Label(new_stud_window, text="name", bg="#161616", fg="white", font=("Times",15,"bold"))
    name.place(relx=0.1, rely=0.34, anchor=W)

    Class = Label(new_stud_window, text="Class", bg="#161616", fg="white", font=("Times",15,"bold"))
    Class.place(relx=0.1, rely=0.41, anchor=W)

    section = Label(new_stud_window, text="section", bg="#161616", fg="white", font=("Times",15,"bold"))
    section.place(relx=0.1, rely=0.48, anchor=W)

    roll_num = Label(new_stud_window, text="RollNum", bg="#161616", fg="white", font=("Times",15,"bold"))
    roll_num.place(relx=0.1, rely=0.55, anchor=W)

    sub1= Label(new_stud_window, text="sub1", bg="#161616", fg="white", font=("Times",15,"bold"))
    sub1.place(relx=0.1, rely=0.62, anchor=W)

    sub2 = Label(new_stud_window, text="sub2", bg="#161616", fg="white", font=("Times",15,"bold"))
    sub2.place(relx=0.1, rely=0.69, anchor=W)

    sub3 = Label(new_stud_window, text="sub3", bg="#161616", fg="white", font=("Times",15,"bold"))
    sub3.place(relx=0.1, rely=0.76, anchor=W)

   
    #Creating Entries:
    ID_entry= Entry(new_stud_window, width=35, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    ID_entry.place(relx=0.9, rely=0.2, anchor=E, height=25)

    session_entry = Entry(new_stud_window, width=35, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    session_entry.place(relx=0.9, rely=0.27, anchor=E, height=25)

    name_entry = Entry(new_stud_window, width=35, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    name_entry.place(relx=0.9, rely=0.34, anchor=E, height=25)

    Class_entry = Entry(new_stud_window, width=35, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    Class_entry.place(relx=0.9, rely=0.41, anchor=E, height=25)
    
    section_entry = Entry(new_stud_window, width=35, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    section_entry.place(relx=0.9, rely=0.48, anchor=E, height=25)

    roll_num_entry = Entry(new_stud_window, width=35, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    roll_num_entry.place(relx=0.9, rely=0.55, anchor=E, height=25)

    sub1_entry = Entry(new_stud_window, width=35, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    sub1_entry.place(relx=0.9, rely=0.62, anchor=E, height=25)

    sub2_entry = Entry(new_stud_window, width=35, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    sub2_entry.place(relx=0.9, rely=0.69, anchor=E, height=25)

    sub3_entry = Entry(new_stud_window, width=35, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    sub3_entry.place(relx=0.9, rely=0.76, anchor=E, height=25)

    #Creating the buttons:
    new_stud_submit_btn = Button(new_stud_window, text="Submit", padx=5, pady=5, font='Ubuntu 15 bold', bg="#161616", fg="white", command=submit)
    new_stud_submit_btn.place(relx=0.5, rely=0.85,anchor=CENTER)

    new_stud_go_back_btn= Button(new_stud_window, text="BACK", command=new_stud_window.destroy, padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white")
    new_stud_go_back_btn.place(relx=0.9, rely=0.97,anchor=S)




def find_stud():
    #Making my entry & window variable global:
    global find_stud_entry
    global find_stud_window

    #Creating window:
    find_stud_window = Toplevel()
    find_stud_window.title("Find student")
    find_stud_window.iconbitmap("favicon.ico")
    find_stud_window.config(bg="#161616")
    find_stud_window.minsize(550,550)
    find_stud_window.maxsize(550,550)

    #Creating Label:
    find_stud_label = Label(find_stud_window, text="ID:", bg="#161616", fg="white", font=("Times",20,"bold"))
    find_stud_label.place(relx=0.39,rely=0.4,anchor=CENTER)
    
    #Creating Entry field:
    find_stud_entry = Entry(find_stud_window, width=10, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    find_stud_entry.place(relx=0.58, rely=0.4, anchor=CENTER, height=30)

    #Creating the Submit button:
    find_stud_submit_btn = Button(find_stud_window, text="Submit", padx=5, pady=5, font='Ubuntu 15 bold', bg="#161616", fg="white", command=submit_2)
    find_stud_submit_btn.place(relx=0.5, rely=0.6,anchor=CENTER)

    #Creating a title or header:
    title_text = Label(find_stud_window, text="Find A Student", font=("Cambria",20,UNDERLINE), bg="#161616", fg="white")
    title_text.place(relx=0.5, rely=0.1, anchor=CENTER)

    #Creating the back button:
    button_back = Button(find_stud_window, text="BACK", command=find_stud_window.destroy, padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white")
    button_back.place(relx=0.9, rely=0.97,anchor=S)

    #Adding illustrations:
    img = Image.open("search.png")
    resize = img.resize((60, 60), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(resize)
    my_label = Label(find_stud_window, image=my_img, border=0)
    my_label.place(relx=0.39, rely=0.87, anchor=CENTER)
    
    img2 = Image.open("search.png")
    resize2 = img2.resize((60, 60), Image.ANTIALIAS)
    my_img2 = ImageTk.PhotoImage(resize2)
    my_label2 = Label(find_stud_window, image=my_img2, border=0)
    my_label2.place(relx=0.16, rely=0.55, anchor=CENTER)

    img4 = Image.open("search.png")
    resize4 = img4.resize((60, 60), Image.ANTIALIAS)
    my_img4 = ImageTk.PhotoImage(resize4)
    my_label4 = Label(find_stud_window, image=my_img4, border=0)
    my_label4.place(relx=0.85, rely=0.23, anchor=CENTER)

    find_stud_window.mainloop()

def submit_2():
    try:

        #Connecting to the database:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
        my_cursor = mydb.cursor()

        #Inserting into the table:
        output = ""
        my_cursor.execute(f"Select * from student1 where ID={find_stud_entry.get()}")
        data = my_cursor.fetchall()
        for i in data:
            output += str(i[0]) + "   " + str(i[1]) + "   " + str(i[2]) + "   " + str(i[3]) + "   " + str(i[4]) + "   " + str(i[5]) + "   " + str(i[6]) + "   " + str(i[7]) + "   " + str(i[8]) + "\n\n"


        #Creating label:
        submit_2_label = Label(find_stud_window, text=output, bg="#161616", fg="white", font=("Cambria",12,"bold"))
        submit_2_label.place(relx=0.5,rely=0.75,anchor=CENTER)
        mydb.commit()
        mydb.close()

        #Clear the text box:
        find_stud_entry.delete(0,END)
    except:
         #Creating a lil popup mssg:
        def popup22():
            messagebox.showerror("Status", "Entry not filled")  
        popup22() 

def delete():
    try:

        #Connecting to the database:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
        my_cursor = mydb.cursor()

        #Deleting a record from the table:
        my_cursor.execute(f"delete from student1 where ID ={int(del_stud_entry.get())} ")
        def pop_del_mssg():
            messagebox.showinfo("Status", "DONE!")  
        pop_del_mssg()
        mydb.commit()
        mydb.close()

        #Clear the text box:
        del_stud_entry.delete(0,END)
    except:
         #Creating a lil popup mssg:
        def popup33():
            messagebox.showerror("Status", "Entry not filled")  
        popup33() 

def del_stud():
    #Making my entry & window variable global:
    global del_stud_entry
    global del_stud_window

    #Creating window:
    del_stud_window = Toplevel()
    del_stud_window.title("Delete")
    del_stud_window.iconbitmap("favicon.ico")
    del_stud_window.config(bg="#161616")
    del_stud_window.minsize(550,550)
    del_stud_window.maxsize(550,550)

    #Creating Label:
    del_stud_label = Label(del_stud_window, text="ID:", bg="#161616", fg="white", font=("Times",20,"bold"))
    del_stud_label.place(relx=0.39,rely=0.4,anchor=CENTER)
    
    #Creating Entry field:
    del_stud_entry = Entry(del_stud_window, width=10, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    del_stud_entry.place(relx=0.6, rely=0.4, anchor=CENTER, height=30)

    #Creating the Delete button:
    del_stud_submit_btn = Button(del_stud_window, text="Delete", padx=5, pady=5, font='Ubuntu 15 bold', bg="#161616", fg="white", command=delete)
    del_stud_submit_btn.place(relx=0.5, rely=0.6,anchor=CENTER)

    #Creating a title or header:
    title_text = Label(del_stud_window, text="Lets Delete A Student", font=("Cambria",20,UNDERLINE), bg="#161616", fg="white")
    title_text.place(relx=0.5, rely=0.1, anchor=CENTER)

    #Creating the back button:
    button_back = Button(del_stud_window, text="BACK", command=del_stud_window.destroy, padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white")
    button_back.place(relx=0.9, rely=0.97,anchor=S)

    #Adding Illustrations
    
    img = Image.open("trash.png")
    resize = img.resize((60, 60), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(resize)
    my_label = Label(del_stud_window, image=my_img, border=0)
    my_label.place(relx=0.7, rely=0.7, anchor=CENTER)
    
    img2 = Image.open("trash.png")
    resize2 = img2.resize((60, 60), Image.ANTIALIAS)
    my_img2 = ImageTk.PhotoImage(resize2)
    my_label2 = Label(del_stud_window, image=my_img2, border=0)
    my_label2.place(relx=0.16, rely=0.45, anchor=CENTER)

    img4 = Image.open("trash.png")
    resize4 = img4.resize((60, 60), Image.ANTIALIAS)
    my_img4 = ImageTk.PhotoImage(resize4)
    my_label4 = Label(del_stud_window, image=my_img4, border=0)
    my_label4.place(relx=0.85, rely=0.23, anchor=CENTER)

    del_stud_window.mainloop()


