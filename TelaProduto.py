class TelaProdutos:

    def opçoes(self):
        opçao = int(input("\n0 - Voltar \n1 - Inserir produto \n2 - Excluir produto \n3 - Listar produtos\n"))
        return opçao

    def pegar_info(self):
        while True:
            codigo,nome,preco = input("\nQual o código, nome e preço do produto que deseja registrar?: ").split()

            if not codigo.isnumeric() or not preco.isnumeric():
                print("Código e preço devem ser numéricos e nome em palavras!")
            else:
                return codigo,nome,preco
    
    def mostrar_info(self, produto):
        print("Código:", produto.codigo, "| Nome:", produto.nome,"| Preço: R$", produto.preco)

    def selecionar_produto(self, produtos):
        for produto in produtos:
            print("Código:", produto.codigo, "| Nome:", produto.nome,"| Preço: R$", produto.preco)
        codigo = int(input("Digite o código do produto: "))
        return codigo

    def printar(self, texto):
        print(texto)

    
        