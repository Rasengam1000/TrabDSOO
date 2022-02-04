class TelaCarrinho:

    def opçoes(self):
        while True:
            opçao = int(input("\n0 - Voltar \n1 - Inserir compra \n2 - Excluir compra \n3 - Listar compras\n"))
            
            if opçao > 3 or opçao < 0:
                print("A opção deve estar entre 0 e 3")
            else: 
                return opçao


    def pegar_info(self):
        while True:
            cpf = input("Qual o CPF do cliente (sem pontos)?: ")

            if not cpf.isnumeric():
                print("CPF deve ser numérico!")
            else:
                return int(cpf)


    def mostrar_produtos(self, produtos):
        print("Produtos disponíveis: ")
        i=0
        for produto in produtos:
            i += 1
            print(i, "- Código:", produto.codigo, "| Nome:", produto.nome,"| Preço: R$", produto.preco)

        while True:
            escolha = int(input("Selecione um produto: "))
            if escolha < 1 or escolha > len(produtos):
                print(f"O número escolhido deve estar entre 1 e {len(produtos)}")
            else:
                return produtos[escolha-1]


    def mostrar_info(self, compras):
        for i in range(len(compras)):
            print(i+1, "-", compras[i].nome)

        while True:
            escolha = int(input("Qual produto deseja excluir?: "))

            if escolha < 1 or escolha > len(compras):
                print(f"O número escolhido deve estar entre 1 e {len(compras)}")
            else:
                return compras[escolha-1]
        

    def mostrar_carrinho(self, compras):
        for produto in compras:
            print("\nCódigo:", produto.codigo, "| Nome:", produto.nome,"| Preço: R$", produto.preco)


    def printar(self, texto):
        print(texto)

    def mostrar_extrato(self,extrato,total):
        print(f"".ljust(39,"-"))

        for linha in extrato:         #imprime o extrato
            print(f"| {linha:35} |")

        print(f"| Total: R${total:29} |")
        print(f"".ljust(39,"-"))
