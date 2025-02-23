langs={
    "pt-br":{
        1:"Senha sem Título",
        2:"NOVA SENHA"
    },
    "en-us":{
        1:"Untitled password",
        2:"NEW PASSWORD"
    }
}

class Lang:
    def __init__(self,name = "en-us"):
        self.name=name
        self.langWords= langs[name]
        pass

    def updateLang(self,newName):
        self.name = newName
        self.getWord = langs[newName]
