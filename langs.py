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
        12:'TempMail'
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
        12:"TempMail"
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
