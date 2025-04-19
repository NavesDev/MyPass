import langs;
from customtkinter import *;
from PIL import Image,ImageTk;
from frontElements import *;
from myScripts import dataSave,dataDecodify;
import tkinter

background="#1F1F1F"
myLang=langs.Lang()
myWords = myLang.langWords
myWindows = newWindowsPack()
subPadsX=10
configPadsX=20
userSettings = dataDecodify("userSettings")

def closeWindowFunc(window):
    def closeW():
        window.destroy()
    return closeW

def newHeader(root):
    mousePos = {'x':0,'y':0}
    def close_window():
        root.quit()

    def minimize_window():
        #root.iconify()
        root.withdraw()

    def move_window(e):
        root.geometry(f"+{e.x_root+mousePos['x']}+{e.y_root+mousePos['y']}")
    
    def startMove(e):
        lastPos = {}
        xwin = root.winfo_x()
        ywin = root.winfo_y()
       
        mousePos['y'] = ywin - e.y_root
        mousePos['x'] = xwin - e.x_root

    header = CTkFrame(root,height=30,corner_radius=10,fg_color="#242424",)
    header.pack(fill='x',side='top')
    header.bind("<Button-1>",startMove)
    header.bind("<B1-Motion>",move_window)


    img = newCTkImg("assets/images/clsB.png",{'x':14,'y':14})
    closeB = CTkButton(header,width=30,height=30,text='',command=close_window,fg_color='transparent',hover_color='red',image=img)
    closeB.pack(side='right')

    img = newCTkImg("assets/images/minB.png",{'x':14,'y':14})
    minimB = CTkButton(header,width=30,height=30,text='',command=minimize_window,fg_color='transparent',hover_color='#343434',image=img)
    minimB.pack(side='right')
    return header

def newPassWindow():
        pw=CTkToplevel()
        myWindows.newWindow(pw)
        pw.title(myWords[3])
    
        pw.geometry("200x300")
        pw.resizable(False,False)
        pw.maxsize(width=200,height=300)
        pw.minsize(width=200,height=300)
        
        header = CTkFrame(pw,corner_radius=5,width=200,height=30)
        header.pack(fill='x',pady=5)
    
        scrFrame = CTkScrollableFrame(pw, width=200,height=220)
        scrFrame.pack()
        
        saveButton = CTkButton(pw,text=myWords[7],fg_color='#E0A307',font=('Poppins Bold',16),hover_color='#C08B06',width=200,corner_radius=5,height=30)
        
        saveButton.pack(fill='x',pady=0)

        backIcon = Image.open('assets/icons/backButton.png')
        backIcon.resize((16,16))
        backIcon= CTkImage(backIcon)
     
        backButton = CTkButton(header,text="",image=backIcon,width=16,height=16,fg_color="transparent",hover_color="#E0A307",command=closeWindowFunc(pw))
        backButton.place(relx=0,rely=0.5,anchor='w')

        CTkLabel(header,text=myWords[3],font=("poppins regular",15)).pack()#.place(relx='0.5',rely='0.5',anchor="center")

        CTkLabel(scrFrame,text=myWords[5],font=("poppins semibold",15)).pack(pady=1)

        inpTitle=CTkEntry(scrFrame,font=("poppins semibold",14),placeholder_text=f"({myWords[6]})")
        inpTitle.pack(pady=3) 

        CTkLabel(scrFrame,text=myWords[4]+"*",font=("poppins semibold",15)).pack(pady=1)
        
        inpSenha=CTkEntry(scrFrame,font=("poppins semibold",14))
        inpSenha.pack(pady=3) 

        CTkLabel(scrFrame,text="Email",font=("poppins semibold",15)).pack(pady=1)
        
        inpEmail=CTkEntry(scrFrame,font=("poppins semibold",14),placeholder_text=f"({myWords[6]})")
        inpEmail.pack(pady=3) 
        
        CTkLabel(scrFrame,text="Website",font=("poppins semibold",15),).pack(pady=1)

        
        inpWebsite=CTkEntry(scrFrame,font=("poppins semibold",14),placeholder_text=f"({myWords[6]})")
        inpWebsite.pack(pady=3) 

        pw.grab_set()
        pw.mainloop()





def window1():
    window = tkinter.Tk()
    myWindows.newWindow(window)
    window.config(background="#242424")
    window.title("MyPass")
    window.maxsize(width=550,height=500)
    window.minsize(width=550,height=500)
    window.resizable(False,False)
    set_appearance_mode("dark")
    window.geometry("600x500+200+200")
    
   
    

    window.overrideredirect(True)

    
    newHeader(window)

    
    

    
    
    ##label1 = tk.Label(window,text="User",font=("Poppins Medium",20))
    

    tab1 = CTkFrame(window,width=370,height=460)
    
    frame = CTkFrame(tab1,fg_color='transparent')
    frame.place(relx=0.5,rely=0.5,anchor='center')
    title = CTkLabel(frame,font=("poppins semibold",24))
    title.pack(side='top')
    myLang.setObjWord(title,13)

    version=CTkLabel(frame,font=("poppins regular",16))
    version.pack(side='top')
    myLang.setObjWord(version,14)
    

    tab2 = CTkFrame(window,width=370,height=460)
    
    scrFrame = CTkScrollableFrame(tab2,width=350,height=440,fg_color='transparent')
    scrFrame.place(anchor="center",relx="0.5",rely="0.5")
    
    title = CTkLabel(scrFrame,font=("poppins medium",20))
    title.pack(side='top',pady=5)
    myLang.setObjWord(title,8)
    
    
    subtitle = CTkLabel(scrFrame,font=("poppins regular",18))
    subtitle.pack(side='top',anchor='w',padx=subPadsX)
    myLang.setObjWord(subtitle,15)


    hold = newSupportFrame(scrFrame)
    hold.pack(side='top',anchor='w',padx=configPadsX)

    optLabel = CTkLabel(hold,font=("poppins",16))
    optLabel.pack(side='left',padx=5)
    myLang.setObjWord(optLabel,16)

    
    opts = langs.getLangsNames("upper")
    def updLang(choice):
        myLang.updateLang(choice)
    opMenu = newOpMenu(hold)
    opMenu.configure(values=opts,command=updLang)
    
    opMenu.set(langs.getSelectedLang().upper())
    opMenu.pack(side='left')

    tab3 = CTkFrame(window,width=370,height=460)

    tab4 = CTkFrame(window,width=370,height=460)

    tab5 = CTkFrame(window,width=370,height=460)
    
    tab6 = CTkFrame(window,width=370,height=460)

    CTkLabel(tab3,text="Teste3",font=("poppins semibold",15)).place(relx='0.5',rely='0.5',anchor='center')
    newTab=MyTab(tab1,"welcome",{"relx":'1',"rely":"0","anchor":"ne","x":-5,"y":35})
    newTab.addTab(tab2,"configs")
    newTab.addTab(tab3,"security")
    newTab.addTab(tab4,'passwords')
    newTab.addTab(tab5,'updates')
    newTab.addTab(tab6,'tempE')
    #button = CTkButton(scrFrame,text="+ "+myWords[2],font=('Poppins Bold',16),corner_radius=7,fg_color="#E0A307",hover_color="#C08B06",command=newPassWindow)
    #button.grid(row=0,column=0,padx=10)


    frame1 = CTkFrame(window,width=170,height=500,corner_radius=0)
    frame1.place(relx="0",rely="0",anchor='nw')
    
    def newMenuB():
        return CTkButton(frame1,text="MENUB",width=160,font=("poppins bold",13),fg_color='#3a3a3a',hover_color="#232323",anchor='w')

    logo = CTkImage(Image.open("assets/images/myLogo.png"),size=(105,38))
    
    logoholder=CTkLabel(frame1,text='',image=logo,anchor='center')
    logoholder.place(y=10,relx=0.5,anchor='n')

    img = newCTkImg("assets/icons/passwordButton.png",{'x':12,'y':12})
    
    button1 = newMenuB()
    button1.configure(command=newTab.linkTab("passwords",button1),image=img)
    myLang.setObjWord(button1,10,'upper')

    myFlex = AutoPlace(button1,40,{'x':0,'y':60,"relx":0.5,"rely":0,'anchor':'n'})

    img = newCTkImg("assets/icons/tempButton.png",{'x':12,'y':12})

    button2 = newMenuB()
    button2.configure(command=newTab.linkTab("tempE",button2),image=img)
    myLang.setObjWord(button2,12,'upper')
    myFlex.addObj(button2)

    img = newCTkImg("assets/icons/securityButton.png",{'x':12,'y':12})

    button2 = newMenuB()
    button2.configure(command=newTab.linkTab("security",button2),image=img)
    myLang.setObjWord(button2,9,'upper')
    myFlex.addObj(button2)


    img = newCTkImg("assets/icons/configButton.png",{'x':12,'y':12})

    button2 = newMenuB()
    button2.configure(command=newTab.linkTab("configs",button2),image=img)
    myLang.setObjWord(button2,8,'upper')
    myFlex.addObj(button2)

    img = newCTkImg("assets/icons/updateButton.png",{'x':12,'y':12})

    button2 = newMenuB()
    button2.configure(command=newTab.linkTab("updates",button2),image=img)
    myLang.setObjWord(button2,11,'upper')
    myFlex.addObj(button2)
    window.mainloop()



