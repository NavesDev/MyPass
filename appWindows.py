import tkinter;
import langs;
from customtkinter import *;
from PIL import Image,ImageTk;

class MyTab():
    def __init__(self,baseTab,tabName,basePlacement):
        self.tabs={
            tabName:baseTab
        }
        self.basePlacement=basePlacement
        bP=basePlacement

        self.selectedTab=tabName
        baseTab.place(x=bP["x"],y=bP['y'],relx=bP['relx'],rely=bP['rely'],anchor=bP['anchor'])
        pass
    def addTab(self,tab,tabName):
        self.tabs[tabName]=tab
        tab.place_forget()
    def changeTab(self,tabName):
        if((tabName in self.tabs) and (tabName!=self.selectedTab)):
            bP=self.basePlacement
            self.tabs[self.selectedTab].place_forget()
            self.tabs[tabName].place(x=bP["x"],y=bP['y'],relx=bP['relx'],rely=bP['rely'],anchor=bP['anchor'])
            self.selectedTab=tabName
    def linkTab(self,tabName):
        
        return lambda: self.changeTab(tabName)
        

background="#1F1F1F"
myLang=langs.Lang("pt-br")
myWords = myLang.langWords

def closeWindowFunc(window):
    def closeW():
        window.destroy()
    return closeW

def window1():
    window = CTk()
    window.title("MyPass")
    window.maxsize(width=550,height=500)
    window.minsize(width=550,height=500)
    window.resizable(False,False)
    set_appearance_mode("dark")
    window.geometry("550x500")
    

    def newPassWindow():
        
        pw=CTkToplevel()
        pw.title(myWords[3])
        pw.geometry="200x300"
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
        
        CTkLabel(scrFrame,text="Website",font=("poppins semibold",15)).pack(pady=1)
        
        inpWebsite=CTkEntry(scrFrame,font=("poppins semibold",14),placeholder_text=f"({myWords[6]})")
        inpWebsite.pack(pady=3) 

        pw.grab_set()
        pw.mainloop()

    

    wintitle = CTkLabel(window,text="MyPass",font=("poppins bold",20))
    wintitle.place(relx="0.5",rely="0",anchor="n")
    
    ##label1 = tk.Label(window,text="User",font=("Poppins Medium",20))
    

    tab1 = CTkFrame(window,width=360,height=490)
    
    scrFrame = CTkScrollableFrame(tab1,width=340,height=470,fg_color='transparent')
    scrFrame.place(anchor="center",relx="0.5",rely="0.5")

    tab2 = CTkFrame(window,width=360,height=490)
    
    tab3 = CTkFrame(window,width=360,height=490)

    newTab=MyTab(tab1,"inicial",{"relx":'1',"rely":"0.5","anchor":"e","x":-5,"y":0})
    newTab.addTab(tab2,"teste1")
    newTab.addTab(tab3,"teste2")
    
    button = CTkButton(scrFrame,text="+ "+myWords[2],font=('Poppins Bold',16),corner_radius=7,fg_color="#E0A307",hover_color="#C08B06",command=newPassWindow)
    button.grid(row=0,column=0,padx=10)


    frame1 = CTkFrame(window,width=170,height=490)
    frame1.place(relx="0",rely="0.5",anchor='w',x=5)
    
    def newMenuB():
        return CTkButton(frame1,text="MENUB",width=150,font=("poppins medium",16),fg_color='#3a3a3a',hover_color="#232323")
    
    button1 = newMenuB()
    button1.configure(text="SENHAS",command=newTab.linkTab("inicial"))
    button1.place(y=10,relx=0.5,anchor='n')

    button2 = newMenuB()
    button2.configure(text=myWords[8].upper(),command=newTab.linkTab("teste1"))
    button2.place(y=50,relx=0.5,anchor='n')
    

    
    window.mainloop()