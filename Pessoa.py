#Classe pessoa criado por Helena Vieira
#No dia 15/09/2018

class Pessoa(object):
    def __init__(self,n,sobre,s):
        self.nome = n
        self.sobrenome = sobre
        self.senha = s
        
    def __str__(self):
        return str(self.nome)
    
    def getNome(self):
        return self.nome
    def setNome(self,n):
        self.nome=n
    def getSobrenome(self):
        return self.sobrenome
    def setSobrenome(self,sobre):
        self.sobrenome=sobre
    def getSenha(self):
        return self.senha
    def setSenha(self,s):
        self.senha=s
        
lista=[]
print(lista)
nome=str(input("Digite seu nome:"))
while(nome!="F"):
    
    sobrenome=str(input("Digite seu sobrenome:"))
    senha=str(input("Digite sua senha:")) 
    pessoa1 = Pessoa(nome,sobrenome,senha)
    lista.append(pessoa1.__str__())
    print(lista)
    print("""Nome:{}
Sobrenome:{}
Senha:{}""".format(nome,sobrenome,senha))
    nome=str(input("Digite seu nome:"))

if(lista[0]==lista[1]):
    print("lindo")
