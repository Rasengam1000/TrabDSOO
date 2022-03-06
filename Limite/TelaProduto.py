from Limite.AbstractTela import AbstractTela

class TelaProdutos(AbstractTela):

    def opcoes(self):
        print("\n----------- Produtos -----------\n1 - Inserir produto \n2 - Excluir produto"
                "\n3 - Listar produtos \n0 - Voltar ")

        opçao = self.verifica_num_int("Escolha a opção: ", [0,1,2,3])

        return opçao

    def pegar_info(self):
        while True:
            try:
                codigo,nome,preco = input("\nQual o código, nome e preço do produto que deseja registrar?: ").split()
                if not codigo.isnumeric() or not preco.isnumeric():
                    print("Código e preço devem ser numéricos!")
                else:
                    return codigo,nome,preco
            except:
                break

    
    def mostrar_info(self, produto):
        print("Código:", produto.codigo, "| Nome:", produto.nome,"| Preço: R$", produto.preco)
    

    def mostrar_produtos(self, produtos):
        print("Produtos disponíveis: ")
        i=0
        for produto in produtos:
            i += 1
            print(f"\n{i}", "| Nome:", produto.nome,"| Preço: R$", produto.preco)

        while True:
            escolha = int(input("\nSelecione um produto: "))
            if escolha < 1 or escolha > len(produtos):
                print(f"O número escolhido deve estar entre 1 e {len(produtos)}")
            else:
                return produtos[escolha-1]


    def selecionar_produto(self, produtos):
        for produto in produtos:
            print("Código:", produto.codigo, "| Nome:", produto.nome,"| Preço: R$", produto.preco)
            
        codigo = int(input("Digite o código do produto: "))

        return codigo

    def printar(self, texto):
        print(texto)

    
        