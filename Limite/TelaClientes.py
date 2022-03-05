from limite.AbstractTela import AbstractTela

class TelaClientes(AbstractTela):

    def opcoes(self):
        print('\n----------- Clientes -----------')
        print('1 - Incluir Cliente')
        print('2 - Excluir Cliente')
        print('3 - Alterar Cadastro')
        print('4 - Informacao Cliente')
        print('5 - Listar Clientes')
        print('0 - Retornar')
        opcao = self.verifica_num_int('Escolha a opção: ', [1, 2, 3, 4, 5, 0])
        return opcao

    def pegar_info(self):
        print('\nDados Cliente')
        nome = self.verifica_letra('Nome: ')
        sobrenome = self.verifica_letra('Sobrenome: ')
        cpf = self.verifica_algarismo('CPF: ')
        idade = self.verifica_algarismo('Idade: ')
        tipo_cliente = self.verifica_resposta('Seria cliente vip ou comum?: ', ['vip', 'comum'])

        return{'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'idade': idade, 'tipo_cliente': tipo_cliente}

    def mostrar_info(self, dados_cliente):
        print('\nNome do Cliente: ', dados_cliente['nome'])
        print('Sobrenome do Cliente: ', dados_cliente['sobrenome'])
        print('CPF do Cliente: ', dados_cliente['cpf'])
        print('Idade do Cliente: ', dados_cliente['idade'])
        print('Tipo do CLiente: ', dados_cliente['tipo_cliente'])

    def selecionar_cliente(self):
        cpf = self.verifica_algarismo('CPF do cliente desejado: ')
        return cpf