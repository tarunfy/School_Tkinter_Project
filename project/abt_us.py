from tkinter import *
import webbrowser

def callback(url):
    edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
    webbrowser.get(edge_path).open_new_tab(url)
   


    # root = Tk()
    # link1 = Label(root, text="Tarun", fg="blue", cursor="hand2")
    # link1.pack()
    # link1.bind("<Button-1>", lambda e: callback("tarun2506.github.io"))

    # link2 = Label(root, text="Ecosia Hyperlink", fg="blue", cursor="hand2")
    # link2.pack()
    # link2.bind("<Button-1>", lambda e: callback("http://www.ecosia.org"))

    # root.mainloop()