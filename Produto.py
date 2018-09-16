class Produto:
    def __init__(self,nome,quantidade,preco):
        self.nome = nome
        self.quantidade = int(quantidade)
        self.preco = float(preco)
        
    def __str__(self):
        return f'Nome:{self.nome}'
    
    def getNome(self):
        return self.nome
    def setNome(self,nome):
        self.nome = nome

    def getQuantidade(self):
        return self.quantidade
    def setQuantidade(self,quantidade):
        self.quantidade = quantidade

    def getPreco(self):
        return self.preco       
    def setPreco(self,preco):
        self.nome = preco

  
#teste de produto
        
listaDeProdutos=[]
carrinho = []

print("####Teste de produto####")

nome = str(input("Nome do produto:"))

while(nome != "f" ):
    quantidade = int(input("Quantidade:"))
    preco = float(input("Preço:"))
    
    novoProduto = Produto(nome,quantidade,preco)
    listaDeProdutos.append(novoProduto)
    carrinho.append(novoProduto.__str__())
    print("A carrinho de produtos:{}".format(carrinho))
    
    nome = str(input("Digite o nome do produto:"))


print("-_-LISTA DE PRODUTOS-_-")
tamanho = int(len(listaDeProdutos))
precoTotal = 0

for i in range(tamanho):
    
    print("""Nome:{:>15}    Quantidade:{}  X  Preço:{}  = {} \n""".format(listaDeProdutos[i].getNome(),listaDeProdutos[i].getQuantidade(),listaDeProdutos[i].getPreco(),listaDeProdutos[i].getQuantidade()*listaDeProdutos[i].getPreco()))
    precoTotal =   precoTotal + listaDeProdutos[i].getQuantidade()*listaDeProdutos[i].getPreco()

print("Preço total de produtos = {}".format(precoTotal))
    
    
