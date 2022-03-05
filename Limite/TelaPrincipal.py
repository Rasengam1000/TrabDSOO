from limite.AbstractTela import AbstractTela

class TelaPrincipal(AbstractTela):

    def opcoes(self):
        print('\n----------- Balada ----------')
        print('Escolha sua opcao')
        print('1 - Clientes')
        print('2 - Produtos')
        print('3 - Carrinho')
        print('0 - Encerrar Sistema')
        opcao = self.verifica_num_int('Escolha a opção: ', [1, 2, 3, 0])
        return opcao