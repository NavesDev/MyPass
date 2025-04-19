import random,string,json,os;


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
    def __init__(self,password,email="",title="#default",username=""): 
        addEmail(email)
        self.passW = password
        self.title=title
        self.email=email
        self.username=username
        pass
    def update(self,senha,title="#default",email="",username=""):
        self.title = title
        self.passW = senha
        self.email = email
        self.username = username
        pass

dataLocal = "assets/data"
dataSettings = {};
try:
    with open(f"dataSettings.json","r") as r:
        dataSettings = json.load(r)
except FileNotFoundError:
    raise FileNotFoundError("dataSettings not found!");
except Exception:
    raise Exception("error getting dataSettings!");

def dataDefaultify(dataName,atual = False):
    try:
        if(atual):
            for i in dataSettings[dataName]:
                if(not(atual.get(i) and dataSettings[dataName][i].get("default"))):
                    atual[i] = dataSettings[dataName][i]['default']
        else:
            atual = {}
            for i in dataSettings[dataName]:
                if(dataSettings[dataName][i].get("default")):
                    atual[i] = dataSettings[dataName][i]['default']
        return atual
    except Exception:
        return False;

def propsVerifys(value,props):    
    if("<#lowerCase>") in props:
        if(props["<#lowerCase>"]=="all"):
            value = value.lower()
    elif("<#upperCase>") in props:
        if(props["<#upperCase>"]=="all"):
            value = value.upper()
        elif(props["<#upperCase>"]=="onlyFirst"):
            value = value.capitalize()
        elif(props["<#upperCase>"]=="requiredFirst"):
            value = value[0].upper()+value[1:]
    
    if(("<#validEnters>" in props and value not in props["<#validEnters>"]) or ("<#invalidEnters>" in props and value in props["<#invalidEnters>"])):
        return False
    return value

def dataSave(dataName,dataChanged):
    
    def execute():
        try:
            with open(f"{dataLocal}/{dataName}.json","w") as w:
                changes = {}
                for i in dataChanged:
                    if(dataSettings[dataName].get(i) and dataSettings[dataName][i].get("props")):
                        props = dataSettings[dataName][i]['props']
                        value = propsVerifys(dataChanged[i],props)
                        if(value):
                            changes[i] = value
                
                data = None
                try:
                    data = json.load(w)
                except:
                    data = {}
                for i in changes:
                    data[i] = changes[i]
                json.dump(data,w,indent=4)
                return True
        except Exception:
            return False
    if os.path.exists(dataLocal): 
        return execute()
    else:
        os.makedirs(dataLocal,exist_ok=True)
        return execute()
    

def dataDecodify(dataName):
    def execute():
        try:
            with open(f"{dataLocal}/{dataName}.json","r") as r:
                jsondata = json.load(r)
                jsondata = dataDefaultify(dataName,jsondata)
                return jsondata
        
        except Exception:
            data = dataDefaultify(dataName)
            if(data):
                dataSave(dataName,data)
            return data
    if os.path.exists(dataLocal): 
        return execute()
    else:
        os.makedirs(dataLocal,exist_ok=True)
        return execute()