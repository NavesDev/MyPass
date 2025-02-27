from PIL import Image;
from customtkinter import *;

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
    img.resize((size['x'],size['y']))
    return CTkImage(img)