import langs,tkinter as tk;
from tkinter import ttk
from customtkinter import *;
from PIL import Image;

background="#1F1F1F"
myLang=langs.Lang("pt-br")
myWords = myLang.langWords



def window1():
    window = CTk()
    window.title("MyPass")
    window.maxsize(width=600,height=500)
    window.minsize(width=550,height=500)
    set_appearance_mode("dark")


    window.geometry("550x500")

    wintitle = CTkLabel(window,text="MyPass",font=("poppins bold",20))
    wintitle.place(relx="0.5",rely="0",anchor="n")
    
    ##label1 = tk.Label(window,text="User",font=("Poppins Medium",20))
    
    frame1 = CTkScrollableFrame(window,width=200,height=400,bg_color=background)
    frame1.place(relx="0",x=30,rely="0.5",anchor='w')
    
    
    frame = CTkScrollableFrame(window,width=200,height=400,bg_color=background) 
    frame.place(relx="1",rely="0.5",x=-30,anchor="e")

    button = CTkButton(frame1,text="+ "+myWords[2],font=('Poppins Bold',16),corner_radius=7,fg_color="#E0A307",)
    button.pack(fill='x',pady=3)

    window.mainloop()

window1()