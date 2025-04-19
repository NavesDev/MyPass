from appData import appVersion

langs={
    "pt-br":{
        1:"Senha sem Título",
        2:"NOVA SENHA",
        3:"Nova Senha",
        4:"Senha",
        5:"Título",
        6:"Opcional",
        7:"Salvar",
        8:"Configurações",
        9:"Segurança",
        10:"Senhas",
        11:"Atualizações",
        12:'TempMail',
        13:"Bem-vindo",
        14:"Versão : " + str(appVersion()),
        15:"Programa",
        16:"Língua :"
    },
    "en-us":{
        1:"Untitled password",
        2:"NEW PASSWORD",
        3:"New Password",
        4:"Password",
        5:"Title",
        6:"Optional",
        7:"Save",
        8:"Settings",
        9:"Security",
        10:"Passwords",
        11:"Updates",
        12:"TempMail",
        13:"Welcome",
        14:"Version : " + str(appVersion),
        15:"Program",
        16:"Lang :"
    }
}

selected_lang='pt-br'

def getLangsNames(textConfig = 'None'):
    keys= list(langs.keys())
    if textConfig=="upper":
        for index,key in enumerate(keys):
            keys[index]=key.upper()

    return keys

def getSelectedLang():
    return selected_lang

def priv__wordSet(obj,word,textConfig="none"):
    if(textConfig=="upper"):
        word = word.upper()
    elif(textConfig=="lower"):
        word = word.lower()
    try:
        obj.configure(text=word)
    except:
        print("Got translate error")

class Lang:
    
    def __init__(self):
        global selected_lang
        self.langWords= langs[selected_lang]
        self.Elements=[]
        pass
    
    def setObjWord(self,obj,wordIndex,textConfig = "None"):
        
        word=self.langWords[wordIndex]
        priv__wordSet(obj,word,textConfig)
        self.Elements.append([obj,wordIndex,textConfig])

    def updateLang(self,newName):
        newName = newName.lower()
        global selected_lang
        if ((selected_lang !=newName) and (newName in getLangsNames())):
            selected_lang = newName
            self.langWords = langs[newName]
            for element in self.Elements:
                obj = element[0]
                word = self.langWords[element[1]]
                textConfig = element[2]
                priv__wordSet(obj,word,textConfig)

