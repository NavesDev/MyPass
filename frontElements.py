from PIL import Image;
from customtkinter import *;

class newWindowsPack():
    def __init__(self):
        self.openWindows = []
        pass
    def newWindow(self,window):
        self.openWindows.append(window)
    def closeWindows(self):
        for i in self.openWindows:
            i.quit()
            self.openWindows.remove(i)
    def closeWindow(self,window):
        window.quit()
        self.openWindows.remove(window)

class MyTab():
    def __init__(self,baseTab,tabName,basePlacement):
        self.tabs={
            tabName:baseTab
        }
        self.basePlacement=basePlacement
        self.frozenButtons = False
        bP=basePlacement
        self.lb=False
        self.selectedTab=tabName
        baseTab.place(x=bP["x"],y=bP['y'],relx=bP['relx'],rely=bP['rely'],anchor=bP['anchor'])
        pass
    def addTab(self,tab,tabName):
        self.tabs[tabName]=tab
        tab.place_forget()
    def changeTab(self,tabName,button=False):
        if((tabName in self.tabs) and (tabName!=self.selectedTab)):
            if(self.lb):
                self.lb.configure(text_color="white",border_width=0)
                self.lb=False
            if(button):    
                self.lb = button
                button.configure(text_color='#F5EB87',border_color='#F5EB87',border_width=1.4)

            bP=self.basePlacement
            self.tabs[self.selectedTab].place_forget()
            self.tabs[tabName].place(x=bP["x"],y=bP['y'],relx=bP['relx'],rely=bP['rely'],anchor=bP['anchor'])
            self.selectedTab=tabName
    def linkTab(self,tabName,button=False):
        def func():
            if(not(self.frozenButtons)):
                self.changeTab(tabName,button)
        return func
    def freezeButtons(self):
        self.frozenButtons=True
    def unfreezeButtons(self):
        self.frozenButtons=False
        
class AutoPlace():
    def __init__(self,firstObj,gap,basePos={"x":0,"y":0,"relx":0.5,'rely':0.5,'anchor':"center"},direction='y',wrap=False,wrapNumber=0,wrapGap=20):
        self.basePos=basePos
        self.gap=gap
        self.dir=direction    
        self.wrap=wrap
        #if(wrap):
            #self.wrapBarrier=wrapNumber
            #self.wrapGap=wrapGap
        bp=basePos
        
        firstObj.place(x=bp['x'],y=bp['y'],relx=bp['relx'],rely=bp['rely'],anchor=bp['anchor'])
        pass
    def addObj(self,obj):
        self.basePos[self.dir]=self.basePos[self.dir]+self.gap
        bp=self.basePos
        obj.place(x=bp['x'],y=bp['y'],relx=bp['relx'],rely=bp['rely'],anchor=bp['anchor'])

def newCTkImg(local,size={'x':0,'y':0}):
    img = Image.open(local)
    if(not(size==False)):
        img.resize((size['x'],size['y']))
    return CTkImage(img)

def newSupportFrame(master):
    return CTkFrame(master,fg_color='transparent')

def newOpMenu(master):
    return CTkOptionMenu(master,fg_color="#444444",button_color='#666666',button_hover_color="#555555",font=('poppins medium',13),dropdown_font=('poppins medium',13))