from Limite.AbstractTela import AbstractTela
import time

class TelaCarrinho(AbstractTela):

    def opcoes(self):
        print("\n----------- Carrinho ----------\n1 - Incluir compra \n2 - Excluir compra" 
                "\n3 - Listar compras\n4 - Pagamento \n0 - Voltar")
        
        opçao = self.verifica_num_int("Escolha a opção: ", [0,1,2,3,4])

        return opçao


    def mostrar_info(self, compras):
        for i in range(len(compras)):
            print(f"\n{i+1}", "-", compras[i].nome)

        while True:
            escolha = int(input("\nQual produto deseja excluir?: "))

            if escolha < 1 or escolha > len(compras):
                print(f"O número escolhido deve estar entre 1 e {len(compras)}")
            else:
                return compras[escolha-1]
        

    def mostrar_carrinho(self, compras):
        for produto in compras:
            print("\nCódigo:", produto.codigo, "| Nome:", produto.nome,"| Preço: R$", produto.preco)


    def printar(self, texto):
        print(texto)

    def formas_pagamento(self):
        forma  = self.verifica_num_int("\nQual forma de pagamento deseja utilizar?:\n1 - Cartão \n2 - Dinheiro \n",
                                        [1,2])

        print("Aguardando Pagamento...")
        time.sleep(2)
        pagou = self.verifica_resposta("A conta foi paga? (S/N): ", ["S", "N", "s", "n"]).upper()

        return pagou

    def mostrar_extrato(self,extrato,total):
        print(f"".ljust(39,"-"))

        for linha in extrato:         #imprime o extrato
            print(f"| {linha:35} |")

        print(f"".ljust(39,"-"))


        print("\033[1;38;2;0;150;0m" f"\nTotal: R$ {total}" "\033[0m")