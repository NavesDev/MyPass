import random,string,langs;

myWords = langs.Lang("pt-br")
class PassFuncs:
    def passGenerator(passSize=16,passMode="random"):
        if(passMode=="random"):
            allChar = string.ascii_letters+string.digits+"!@#$*-_"
            return "".join(random.choice(allChar) for _ in range(passSize))
        ##elif(passMode=="repass"):


saved = []

def addEmail(email):
        if(not(email in saved)):
            saved.append(email)
def getEmailList():
    return saved

class Password:
    def __init__(self,password,email="",title=myWords[1],username=""): 
        addEmail(email)
        self.passW = password
        self.title=title
        self.email=email
        self.username=username
        pass
    def update(self,senha,title=myWords[1],email="",username=""):
        self.title = title
        self.passW = senha
        self.email = email
        self.username = username

        