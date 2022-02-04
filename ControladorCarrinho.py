from TelaCarrinho import TelaCarrinho
from Carrinho import Carrinho

class ControladorCarrinho:
    def __init__(self, controlador_sistema):
        self.__tela_carrinho = TelaCarrinho()
        self.__controlador_sistema = controlador_sistema


    def incluir_compras(self):
        cpf = self.__tela_carrinho.pegar_info()
        cliente = self.__controlador_sistema.controlador_clientes.escolhe_cliente_por_cpf(cpf)
        
        escolha = self.__tela_carrinho.mostrar_produtos(self.__controlador_sistema.controlador_produtos.produtos)
        cliente.carrinho.compras.append(escolha)
        

    def excluir_compras(self):
        cpf = self.__tela_carrinho.pegar_info()
        cliente = self.__controlador_sistema.controlador_clientes.escolhe_cliente_por_cpf(cpf)

        produto = self.__tela_carrinho.mostrar_info(cliente.carrinho.compras)
        cliente.carrinho.compras.remove(produto)

        self.__tela_carrinho.printar(f"{produto.nome} excluído com sucesso")


    def listar_compras(self):
        cpf = self.__tela_carrinho.pegar_info()
        cliente = self.__controlador_sistema.controlador_clientes.escolhe_cliente_por_cpf(cpf)
        
        self.extrato(cliente)
        #self.__tela_carrinho.mostrar_carrinho(cliente.carrinho.compras)


    def voltar(self):
        self.__controlador_sistema.abre_tela()


    def extrato(self,cliente):
        total = 0
        for produto in cliente.carrinho.compras:       #calculo extrato/preços
            cliente.carrinho.extrato.append(f"{produto.nome} - R$ {produto.preco}")
            total += produto.preco

        self.__tela_carrinho.mostrar_extrato(cliente.carrinho.extrato,total)


    def abre_tela(self):
        lista_opçoes = {0: self.voltar, 1: self.incluir_compras, 2: self.excluir_compras, 
                        3: self.listar_compras}

        while True:
            opçao = self.__tela_carrinho.opçoes()
            funçao = lista_opçoes[opçao]
            funçao()

    