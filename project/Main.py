from tkinter import *
from PIL import ImageTk, Image
import adm_gui
import fee_gui
import abt_us
import stud_gui

# Making the root window i.e. the appliction window:
root = Tk()
root.config(bg="#161616")
root.title("School Management System")
root.iconbitmap("favicon.ico")
root.minsize(700,700)
root.maxsize(700,700)


# Adding image/banner/header to the application:
img = Image.open("Banner.png")
resize = img.resize((600, 200), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(resize)
my_label = Label(image=my_img, border=0)
my_label.pack()

#Adding illustration:
img2 = Image.open("projectphoto3.jpg")
resize2 = img2.resize((400, 400), Image.ANTIALIAS)
my_img2 = ImageTk.PhotoImage(resize2)
my_label2 = Label(image=my_img2, border=0)
my_label2.place(relx=0.65, rely=0.6, anchor=CENTER)

# Creating the buttons:
button_student_data = Button(root, text="New Admission",padx=5, pady=5, font='Ubuntu 12 bold', bg="#161616", fg="white", command=lambda: adm_gui.admission())
button_student_data.place(relx=0.1, rely=0.5, anchor=W)

button_fee_details = Button(root, text="Student Data",padx=5, pady=5, font='Ubuntu 12 bold', bg="#161616", fg="white", command=lambda: stud_gui.Student_details())
button_fee_details.place(relx=0.1, rely=0.6, anchor=W)

button_adm = Button(root, text="Fee Details",padx=5, pady=5, font='Ubuntu 12 bold', bg="#161616", fg="white", command=lambda: fee_gui.fee_menu())
button_adm.place(relx=0.1, rely=0.7, anchor=W)

button_about_us = Button(root, text="About Us",padx=5, pady=5, font='Ubuntu 12 bold', bg="#161616", fg="white", command=lambda: abt_us.callback('https://heylink.me/SystemDefiance/'))
button_about_us.place(relx=0.1, rely=0.8, anchor=W)

button_quit = Button(root, text="QUIT", command=root.quit, padx=5, pady=5, font='Ubuntu 10 bold', bg="#161616", fg="white")
button_quit.place(relx=0.9, rely=0.97,anchor=S)

root.mainloop()

