from tkinter import *
from PIL import ImageTk, Image
import adm_layout
import mysql.connector
from tkinter import messagebox

def admission():
    # Creating the window for admission menu:
    window_admission = Toplevel()
    window_admission.title("Admission")
    window_admission.iconbitmap("favicon.ico")
    window_admission.config(bg="#161616")
    window_admission.minsize(600,600)
    window_admission.maxsize(600,600)

    
    #Creating the display text:
    header = Label(window_admission, text="Hii There!! What Do You Wanna To Do?", bg="#161616", fg="white", font=("Cambria",20))
    header.place(relx=0.5, rely=0.1, anchor=CENTER)

    #Creating the buttons:
    button_new_adm = Button(window_admission, text="New-Adm",padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white", command=new_adm)
    button_new_adm.place(relx=0.5, rely=0.4, anchor=CENTER)

    button_display_details = Button(window_admission, text="Show-Info",padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white", command=adm_layout.run)
    button_display_details.place(relx=0.4, rely=0.5, anchor=CENTER)

    button_find_student = Button(window_admission, text="Find-Stud",padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white",  command=find_stud)
    button_find_student.place(relx=0.6, rely=0.5, anchor=CENTER)

    button_delete_student = Button(window_admission, text="Del-Stud",padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white", command=del_stud)
    button_delete_student.place(relx=0.3, rely=0.6, anchor=CENTER)

    button_update_details = Button(window_admission, text="Upd-Info",padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white", command=upd_info)
    button_update_details.place(relx=0.7, rely=0.6, anchor=CENTER)

    button_go_back= Button(window_admission, text="BACK",padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white", command=window_admission.destroy)
    button_go_back.place(relx=0.9, rely=0.97, anchor=S)

    #Adding illustrations:
    img = Image.open("ques2.jpg")
    resize = img.resize((60, 60), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(resize)
    my_label = Label(window_admission, image=my_img, border=0)
    my_label.place(relx=0.2, rely=0.9, anchor=CENTER)

    
    img2 = Image.open("ques3.jpg")
    resize2 = img2.resize((60, 60), Image.ANTIALIAS)
    my_img2 = ImageTk.PhotoImage(resize2)
    my_label2 = Label(window_admission, image=my_img2, border=0)
    my_label2.place(relx=0.1, rely=0.3, anchor=CENTER)

    img3 = Image.open("ques6.jpg")
    resize3 = img3.resize((60, 60), Image.ANTIALIAS)
    my_img3 = ImageTk.PhotoImage(resize3)
    my_label3 = Label(window_admission, image=my_img3, border=0)
    my_label3.place(relx=0.8, rely=0.7, anchor=CENTER)

    img4 = Image.open("ques5.jpg")
    resize4 = img4.resize((60, 60), Image.ANTIALIAS)
    my_img4 = ImageTk.PhotoImage(resize4)
    my_label4 = Label(window_admission, image=my_img4, border=0)
    my_label4.place(relx=0.9, rely=0.2, anchor=CENTER)


    window_admission.mainloop()

#Creating submit function for data to be saved:
def submit():
    try:

        #Connecting to the database:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
        my_cursor = mydb.cursor()

        #Inserting into the table:
        my_cursor.execute(f"Insert into admission(admission_num,student_name,address,phone_num,student_class) values({admission_num_entry.get()},'{student_name_entry.get()}','{address_entry.get()}',{phone_num_entry.get()},{student_class_entry.get()})")
        mydb.commit()
        mydb.close()

        #Clear the text boxes:
        student_name_entry.delete(0,END)
        admission_num_entry.delete(0,END)
        address_entry.delete(0,END)
        phone_num_entry.delete(0,END)
        student_class_entry.delete(0,END)

        #Creating a lil popup mssg:
        def popup():
            messagebox.showinfo("Status", "Congrats!")  
        popup()  
    except:
         #Creating a lil popup mssg:
        def popup22():
            messagebox.showerror("Status", "ID already exists/Entries not filled")  
        popup22() 

def new_adm():
    #Making our entries variables global:
    global student_name_entry
    global admission_num_entry
    global address_entry
    global phone_num_entry
    global student_class_entry

    #Creating the window for new admission:
    new_adm_window = Toplevel()
    new_adm_window.title("New Admission")
    new_adm_window.iconbitmap("favicon.ico")
    new_adm_window.config(bg="#161616")
    new_adm_window.minsize(550,550)
    new_adm_window.maxsize(550,550)

    #Creating the display text:
    new_adm_header = Label(new_adm_window, text="NEW ADMISSION", bg="#161616", fg="white", font=("Cambria",20,"bold", UNDERLINE))
    new_adm_header.place(relx=0.5, rely=0.1, anchor=CENTER)

    #Creating the lables:
    student_name = Label(new_adm_window, text="Student-Name:", bg="#161616", fg="white", font=("Times",15,"bold"))
    student_name.place(relx=0.1, rely=0.2, anchor=W)

    admission_num = Label(new_adm_window, text="Admission-Num:", bg="#161616", fg="white", font=("Times",15,"bold"))
    admission_num.place(relx=0.1, rely=0.3, anchor=W)

    address = Label(new_adm_window, text="Student-Address:", bg="#161616", fg="white", font=("Times",15,"bold"))
    address.place(relx=0.1, rely=0.4, anchor=W)

    phone_num = Label(new_adm_window, text="Contact-Num:", bg="#161616", fg="white", font=("Times",15,"bold"))
    phone_num.place(relx=0.1, rely=0.5, anchor=W)

    student_class = Label(new_adm_window, text="Student-Class:", bg="#161616", fg="white", font=("Times",15,"bold"))
    student_class.place(relx=0.1, rely=0.6, anchor=W)

    #Creating Entries:
    student_name_entry = Entry(new_adm_window, width=35, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    student_name_entry.place(relx=0.9, rely=0.2, anchor=E, height=25)

    admission_num_entry = Entry(new_adm_window, width=35, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    admission_num_entry.place(relx=0.9, rely=0.3, anchor=E, height=25)

    address_entry = Entry(new_adm_window, width=35, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    address_entry.place(relx=0.9, rely=0.4, anchor=E, height=25)

    phone_num_entry = Entry(new_adm_window, width=35, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    phone_num_entry.place(relx=0.9, rely=0.5, anchor=E, height=25)

    student_class_entry = Entry(new_adm_window, width=35, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    student_class_entry.place(relx=0.9, rely=0.6, anchor=E, height=25)

    #Creating the buttons:
    new_adm_submit_btn = Button(new_adm_window, text="Submit", padx=5, pady=5, font='Ubuntu 15 bold', bg="#161616", fg="white", command=submit)
    new_adm_submit_btn.place(relx=0.5, rely=0.8,anchor=CENTER)

    new_adm_go_back_btn= Button(new_adm_window, text="BACK", command=new_adm_window.destroy, padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white")
    new_adm_go_back_btn.place(relx=0.9, rely=0.97,anchor=S)



def submit_2():
    try:

        #Connecting to the database:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
        my_cursor = mydb.cursor()

        #Inserting into the table:
        output = ""
        my_cursor.execute(f"Select * from admission where admission_num={find_stud_entry.get()}")
        data = my_cursor.fetchall()
        for i in data:
            output += str(i[0]) + "   " + str(i[1]) + "   " + str(i[2]) + "   " + str(i[3]) + "   " + str(i[4]) + "\n\n"


        #Creating label:
        submit_2_label = Label(find_stud_window, text=output, bg="#161616", fg="white", font=("Cambria",12,"bold"))
        submit_2_label.place(relx=0.5,rely=0.75,anchor=CENTER)
        mydb.commit()
        mydb.close()

        #Clear the text box:
        find_stud_entry.delete(0,END)
    except:
         #Creating a lil popup mssg:
        def popup23():
            messagebox.showerror("Status", "Entry not filled")  
        popup23() 



def find_stud():
    #Making my entry & window variable global:
    global find_stud_entry
    global find_stud_window

    #Creating window:
    find_stud_window = Toplevel()
    find_stud_window.title("Information")
    find_stud_window.iconbitmap("favicon.ico")
    find_stud_window.config(bg="#161616")
    find_stud_window.minsize(550,550)
    find_stud_window.maxsize(550,550)

    #Creating Label:
    find_stud_label = Label(find_stud_window, text="Admission-Num:", bg="#161616", fg="white", font=("Times",20,"bold"))
    find_stud_label.place(relx=0.39,rely=0.4,anchor=CENTER)
    
    #Creating Entry field:
    find_stud_entry = Entry(find_stud_window, width=10, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    find_stud_entry.place(relx=0.69, rely=0.4, anchor=CENTER, height=30)

    #Creating the Submit button:
    find_stud_submit_btn = Button(find_stud_window, text="Submit", padx=5, pady=5, font='Ubuntu 15 bold', bg="#161616", fg="white", command=submit_2)
    find_stud_submit_btn.place(relx=0.5, rely=0.6,anchor=CENTER)

    #Creating a title or header:
    title_text = Label(find_stud_window, text="Lets Find A Student", font=("Cambria",20,UNDERLINE), bg="#161616", fg="white")
    title_text.place(relx=0.5, rely=0.1, anchor=CENTER)

    #Creating the back button:
    button_back = Button(find_stud_window, text="BACK", command=find_stud_window.destroy, padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white")
    button_back.place(relx=0.9, rely=0.97,anchor=S)

    #Adding illustrations:
    img = Image.open("search.png")
    resize = img.resize((60, 60), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(resize)
    my_label = Label(find_stud_window, image=my_img, border=0)
    my_label.place(relx=0.3, rely=0.8, anchor=CENTER)

    
    img2 = Image.open("search.png")
    resize2 = img2.resize((60, 60), Image.ANTIALIAS)
    my_img2 = ImageTk.PhotoImage(resize2)
    my_label2 = Label(find_stud_window, image=my_img2, border=0)
    my_label2.place(relx=0.2, rely=0.2, anchor=CENTER)


    img4 = Image.open("search.png")
    resize4 = img4.resize((60, 60), Image.ANTIALIAS)
    my_img4 = ImageTk.PhotoImage(resize4)
    my_label4 = Label(find_stud_window, image=my_img4, border=0)
    my_label4.place(relx=0.9, rely=0.6, anchor=CENTER)

    find_stud_window.mainloop()


def delete():
    try:

        #Connecting to the database:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
        my_cursor = mydb.cursor()

        #Deleting a record from the table:
        my_cursor.execute(f"delete from admission where admission_num ={int(del_stud_entry.get())} ")
        def pop_del_mssg():
            messagebox.showinfo("Status", "DONE!")  
        pop_del_mssg()
        mydb.commit()
        mydb.close()

        #Clear the text box:
        del_stud_entry.delete(0,END)

    except:
        #Creating a lil popup mssg:
        def popup24():
            messagebox.showerror("Status", "Entry not filled")  
        popup24() 

    


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
    del_stud_label = Label(del_stud_window, text="Admission-Num:", bg="#161616", fg="white", font=("Times",20,"bold"))
    del_stud_label.place(relx=0.39,rely=0.4,anchor=CENTER)
    
    #Creating Entry field:
    del_stud_entry = Entry(del_stud_window, width=10, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    del_stud_entry.place(relx=0.69, rely=0.4, anchor=CENTER, height=30)

    #Creating the Submit button:
    del_stud_submit_btn = Button(del_stud_window, text="Delete", padx=5, pady=5, font='Ubuntu 15 bold', bg="#161616", fg="white", command=delete)
    del_stud_submit_btn.place(relx=0.5, rely=0.6,anchor=CENTER)

    #Creating a title or header:
    title_text = Label(del_stud_window, text="Lets Delete A Student", font=("Cambria",20,UNDERLINE), bg="#161616", fg="white")
    title_text.place(relx=0.5, rely=0.1, anchor=CENTER)

    #Creating the back button:
    button_back = Button(del_stud_window, text="BACK", command=del_stud_window.destroy, padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white")
    button_back.place(relx=0.9, rely=0.97,anchor=S)

    #Adding illustrations:
    img = Image.open("trash.png")
    resize = img.resize((60, 60), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(resize)
    my_label = Label(del_stud_window, image=my_img, border=0)
    my_label.place(relx=0.39, rely=0.87, anchor=CENTER)
    
    img2 = Image.open("trash.png")
    resize2 = img2.resize((60, 60), Image.ANTIALIAS)
    my_img2 = ImageTk.PhotoImage(resize2)
    my_label2 = Label(del_stud_window, image=my_img2, border=0)
    my_label2.place(relx=0.16, rely=0.28, anchor=CENTER)

    img4 = Image.open("trash.png")
    resize4 = img4.resize((60, 60), Image.ANTIALIAS)
    my_img4 = ImageTk.PhotoImage(resize4)
    my_label4 = Label(del_stud_window, image=my_img4, border=0)
    my_label4.place(relx=0.9, rely=0.52, anchor=CENTER)

    del_stud_window.mainloop()

def upd_info():
    #Creating the window:
    upd_info_window = Toplevel()
    upd_info_window.title("Update")
    upd_info_window.iconbitmap("favicon.ico")
    upd_info_window.config(bg="#161616")
    upd_info_window.minsize(550,550)
    upd_info_window.maxsize(550,550)

    #Creating labels:
    upd_info_window_title = Label(upd_info_window, text="Hey, Let's Update Something", font=("Cambria",20,UNDERLINE), bg="#161616", fg="white")
    upd_info_window_title.place(relx=0.5,rely=0.1,anchor=CENTER)

    #Creating buttons:
    upd_info_name_btn = Button(upd_info_window, text="Name", bg="#161616", fg="white", padx=5, pady=5, font='Ubuntu 15 bold', command=upd_name)
    upd_info_name_btn.place(relx=0.5,rely=0.38,anchor=CENTER)

    upd_info_address_btn = Button(upd_info_window, text="Address", bg="#161616", fg="white", padx=5, pady=5, font='Ubuntu 15 bold', command=upd_address)
    upd_info_address_btn.place(relx=0.5,rely=0.5,anchor=CENTER)

    upd_info_phone_num_btn = Button(upd_info_window, text="Phone-Num", bg="#161616", fg="white", padx=5, pady=5, font='Ubuntu 15 bold', command=upd_phone_num)
    upd_info_phone_num_btn.place(relx=0.5,rely=0.62,anchor=CENTER)

    #Creating the back button:
    button_back = Button(upd_info_window, text="BACK", command=upd_info_window.destroy, padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white")
    button_back.place(relx=0.9, rely=0.97,anchor=S)

    #Adding illustrations:
    img = Image.open("folder.png")
    resize = img.resize((60, 60), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(resize)
    my_label = Label(upd_info_window, image=my_img, border=0)
    my_label.place(relx=0.39, rely=0.87, anchor=CENTER)
    
    img2 = Image.open("folder.png")
    resize2 = img2.resize((60, 60), Image.ANTIALIAS)
    my_img2 = ImageTk.PhotoImage(resize2)
    my_label2 = Label(upd_info_window, image=my_img2, border=0)
    my_label2.place(relx=0.16, rely=0.55, anchor=CENTER)

    img4 = Image.open("folder.png")
    resize4 = img4.resize((60, 60), Image.ANTIALIAS)
    my_img4 = ImageTk.PhotoImage(resize4)
    my_label4 = Label(upd_info_window, image=my_img4, border=0)
    my_label4.place(relx=0.85, rely=0.23, anchor=CENTER)

    upd_info_window.mainloop()


def upd_name():
    #Making entry and window variable global:
    global upd_name_adm_num_entry
    global upd_name_new_name_entry
    global upd_name_window

    #Creating the window:
    upd_name_window = Toplevel()
    upd_name_window.title("Update-Name")
    upd_name_window.iconbitmap("favicon.ico")
    upd_name_window.config(bg="#161616")
    upd_name_window.minsize(500,500)
    upd_name_window.maxsize(500,500)

    #Creating Labels:
    upd_name_title_label = Label(upd_name_window, text="Update Student's Name", font=("Cambria",20,UNDERLINE), bg="#161616", fg="white")
    upd_name_title_label.place(relx=0.5,rely=0.1,anchor=CENTER)

    upd_name_adm_num_label =  Label(upd_name_window, text="Admission-Number:",  font=("Times",20,"bold"), bg="#161616", fg="white")
    upd_name_adm_num_label.place(relx=0.39,rely=0.4,anchor=CENTER)

    upd_name_new_name_label =  Label(upd_name_window, text="Updated-Name:",  font=("Times",20,"bold"), bg="#161616", fg="white")
    upd_name_new_name_label.place(relx=0.44,rely=0.5,anchor=CENTER)

    #Creating entry boxes:
    upd_name_adm_num_entry = Entry(upd_name_window, width=10, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    upd_name_adm_num_entry.place(relx=0.77,rely=0.4,anchor=CENTER, height=30)

    upd_name_new_name_entry = Entry(upd_name_window, width=15, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    upd_name_new_name_entry.place(relx=0.77,rely=0.5,anchor=CENTER, height=30)

    #Creating a update button:
    upd_name_update_btn = Button(upd_name_window, text="Update",padx=5, pady=5, font='Ubuntu 15 bold', bg="#161616", fg="white", command=update_name_btn)
    upd_name_update_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

    #Creating the back button:
    button_back = Button(upd_name_window, text="BACK", command=upd_name_window.destroy, padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white")
    button_back.place(relx=0.9, rely=0.97,anchor=S)

    
def update_name_btn():
    try:

        #Connecting to the database:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
        my_cursor = mydb.cursor()

        #Query for updating a name of a student:
        my_cursor.execute(f"update admission set student_name='{upd_name_new_name_entry.get()}' where admission_num={upd_name_adm_num_entry.get()}")
        def pop_name_update_mssg():
            messagebox.showinfo("Status", "UPDATED!")  
        pop_name_update_mssg()
        mydb.commit()
        mydb.close()

        #Clear the text box:
        upd_name_adm_num_entry.delete(0,END)
        upd_name_new_name_entry.delete(0,END)
    except:
        #Creating a lil popup mssg:
        def popup23():
            messagebox.showerror("Status", "Student don't exists/Entries not filled")  
        popup23() 


def upd_address():
    #Making entry and window variable global:
    global upd_address_adm_num_entry
    global upd_address_new_address_entry
    global upd_address_window

    #Creating the window:
    upd_address_window = Toplevel()
    upd_address_window.title("Update-Address")
    upd_address_window.iconbitmap("favicon.ico")
    upd_address_window.config(bg="#161616")
    upd_address_window.minsize(500,500)
    upd_address_window.maxsize(500,500)

    #Creating Labels:
    upd_address_title_label = Label(upd_address_window, text="Update Student's Address", font=("Cambria",20,UNDERLINE), bg="#161616", fg="white")
    upd_address_title_label.place(relx=0.5,rely=0.1,anchor=CENTER)

    upd_address_adm_num_label =  Label(upd_address_window, text="Admission-Number:",  font=("Times",20,"bold"), bg="#161616", fg="white")
    upd_address_adm_num_label.place(relx=0.39,rely=0.4,anchor=CENTER)

    upd_address_new_address_label =  Label(upd_address_window, text="Updated-Address:",  font=("Times",20,"bold"), bg="#161616", fg="white")
    upd_address_new_address_label.place(relx=0.411,rely=0.5,anchor=CENTER)

    #Creating entry boxes:
    upd_address_adm_num_entry = Entry(upd_address_window, width=10, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    upd_address_adm_num_entry.place(relx=0.77,rely=0.4,anchor=CENTER, height=30)

    upd_address_new_address_entry = Entry(upd_address_window, width=15, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    upd_address_new_address_entry.place(relx=0.77,rely=0.5,anchor=CENTER, height=30)

    #Creating a update button:
    upd_address_update_btn = Button(upd_address_window, text="Update",padx=5, pady=5, font='Ubuntu 15 bold', bg="#161616", fg="white", command=update_address_btn)
    upd_address_update_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

    #Creating the back button:
    button_back = Button(upd_address_window, text="BACK", command=upd_address_window.destroy, padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white")
    button_back.place(relx=0.9, rely=0.97,anchor=S)

def update_address_btn():
    try:
        #Connecting to the database:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
        my_cursor = mydb.cursor()

        #Query for updating a address of a student:
        my_cursor.execute(f"update admission set address='{upd_address_new_address_entry.get()}' where admission_num={upd_address_adm_num_entry.get()}")
        def pop_address_update_mssg():
            messagebox.showinfo("Status", "UPDATED!")  
        pop_address_update_mssg()
        mydb.commit()
        mydb.close()

        #Clear the text box:
        upd_address_adm_num_entry.delete(0,END)
        upd_address_new_address_entry.delete(0,END)
    except:
        #Creating a lil popup mssg:
        def popup26():
            messagebox.showerror("Status", "Student don't exists/Entries not filled")  
        popup26() 

    
def upd_phone_num():
    #Making entry and window variable global:
    global upd_phone_num_adm_num_entry
    global upd_phone_num_new_phone_num_entry
    global upd_phone_num_window

    #Creating the window:
    upd_phone_num_window = Toplevel()
    upd_phone_num_window.title("Update-Phone-Number")
    upd_phone_num_window.iconbitmap("favicon.ico")
    upd_phone_num_window.config(bg="#161616")
    upd_phone_num_window.minsize(500,500)
    upd_phone_num_window.maxsize(500,500)

    #Creating Labels:
    upd_phone_num_title_label = Label(upd_phone_num_window, text="Update Student's Phone Number", font=("Cambria",20,UNDERLINE), bg="#161616", fg="white")
    upd_phone_num_title_label.place(relx=0.5,rely=0.1,anchor=CENTER)

    upd_phone_num_adm_num_label =  Label(upd_phone_num_window, text="Admission-Number:",  font=("Times",20,"bold"), bg="#161616", fg="white")
    upd_phone_num_adm_num_label.place(relx=0.39,rely=0.4,anchor=CENTER)

    upd_phone_num_new_phone_num_label =  Label(upd_phone_num_window, text="Updated-Phone-Num:",  font=("Times",20,"bold"), bg="#161616", fg="white")
    upd_phone_num_new_phone_num_label.place(relx=0.38,rely=0.5,anchor=CENTER)

    #Creating entry boxes:
    upd_phone_num_adm_num_entry = Entry(upd_phone_num_window, width=10, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    upd_phone_num_adm_num_entry.place(relx=0.77,rely=0.4,anchor=CENTER, height=30)

    upd_phone_num_new_phone_num_entry = Entry(upd_phone_num_window, width=15, bg="#161616", fg="white", font=("Arial", 10, "normal"))
    upd_phone_num_new_phone_num_entry.place(relx=0.77,rely=0.5,anchor=CENTER, height=30)

    #Creating a update button:
    upd_phone_num_update_btn = Button(upd_phone_num_window, text="Update",padx=5, pady=5, font='Ubuntu 15 bold', bg="#161616", fg="white", command=update_phone_num_btn)
    upd_phone_num_update_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

    #Creating the back button:
    button_back = Button(upd_phone_num_window, text="BACK", command=upd_phone_num_window.destroy, padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white")
    button_back.place(relx=0.9, rely=0.97,anchor=S)

def update_phone_num_btn():
    try:

        #Connecting to the database:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
        my_cursor = mydb.cursor()

        #Query for updating phone number of a student:
        my_cursor.execute(f"update admission set phone_num={upd_phone_num_new_phone_num_entry.get()} where admission_num={upd_phone_num_adm_num_entry.get()}")
        def pop_phone_num_update_mssg():
            messagebox.showinfo("Status", "UPDATED!")  
        pop_phone_num_update_mssg()
        mydb.commit()
        mydb.close()

        #Clear the text box:
        upd_phone_num_adm_num_entry.delete(0,END)
        upd_phone_num_new_phone_num_entry.delete(0,END)
    except:
        #Creating a lil popup mssg:
        def popup13():
            messagebox.showerror("Status", "Student don't exists/Entries not filled")  
        popup13() 







