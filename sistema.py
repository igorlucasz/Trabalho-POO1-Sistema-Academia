from datetime import ZoneInfo, datetime

class Aluno:
    def __init__(self, nome, cpf, plano):
        self.nome = nome
        self.cpf = cpf
        self.plano = plano
        self.ficha = FichaDeTreino()

    def get_nome(self):
        return self.nome

class FichaDeTreino:
    def __init__(self):
    
        self.exercicios = []
    
    def ficha_treino(self):
        return self.exercicios

    def adicionar_exercicio(self, exercicio):
        self.exercicios.append(exercicio)

    def remover_exercicio(self, exercicio):
        self.exercicios.remove(exercicio)

class Plano:
    def __init__(self, mensalidade, data_vencimento):
        self.mensalidade = mensalidade
        self.data_vencimento = data_vencimento
    
    def calcular_mensalidade(self):
        pass
    
    def vencimento(self):
        pass

class PlanoMensal(Plano):
    def __init__(self, mensalidade, data_vencimento):
        super().__init__(mensalidade, data_vencimento)
    
    def get_plano(self):
        return 'Mensal'
    
    def calcular_mensalidade(self):
        return self.mensalidade
    
    def vencimento(self):
        ano, mes, dia = list(map(int, self.data_vencimento.split('-')))
        if(mes == 12):
            mes = 1
            ano += 1
        else:
            mes += 1

        return f'{dia}/{mes}/{ano}'

class PlanoTrimestral(Plano):
    def __init__(self, mensalidade, data_vencimento):
        super().__init__(mensalidade,data_vencimento)
    
    def get_plano(self):
        return 'Trimestral'

    def calcular_mensalidade(self):
        return self.mensalidade * 0.9

    def vencimento(self):
        ano, mes, dia = list(map(int, self.data_vencimento.split('-')))
        if(mes > 9):
            mes -= 9
            ano += 1
        else:
            mes += 3
            
        return f'{dia}/{mes}/{ano}'

class PlanoSemestral(Plano):
    def __init__(self, mensalidade, data_vencimento):
        super().__init__(mensalidade, data_vencimento)
    
    def get_plano(self):
        return 'Semestral'

    def calcular_mensalidade(self):
        return self.mensalidade * 0.85

    def vencimento(self):
        ano, mes, dia = list(map(int, self.data_vencimento.split('-')))
        if(mes > 6):
            mes -= 6
            ano += 1
        else:
            mes += 6
            
        return f'{dia}/{mes}/{ano}'

class PlanoAnual(Plano):
    def __init__(self, mensalidade, data_vencimento):
        super().__init__(mensalidade, data_vencimento)
    
    def get_plano(self):
        return 'Anual'

    def calcular_mensalidade(self):
        return self.mensalidade * 0.8

    def vencimento(self):
        ano, mes, dia = list(map(int, self.data_vencimento.split('-')))
        ano += 1
            
        return f'{dia}/{mes}/{ano}'
 
def verifica_plano(x):
    if(x != 'm' and x != 'mensal' and x != 't' and x != 'trimestral' and x != 's' and x != 'semestral' and x != 'a' and x != 'anual'):
        nova_resposta = input('Plano inválido! Digite novamente: ')
        verifica_plano(nova_resposta)
    else:
        return x

clientes = {}
mensalidade = 200
data = datetime.now(ZoneInfo("America/Sao_Paulo")).date()

while(True):
    print('\n------------------------ Sistema Academia POO (Performance Orientada a Objetivos)  ------------------------')

    print('\nOpções:')
    print('1) Registrar aluno')
    print('2) Editar planilha de treino')
    print('3) Verificar aluno')
    print('4) Alterar valor padrão da mensalidade')
    print('5) Sair do sistema')
    opcao = int(input('\nDigite a opção desejada: '))

    match opcao:
        case 1:
            print('\nDigite as informações necessárias')
            nome = input('\nnome:')
            cpf = int(input('CPF:'))
            plano = verifica_plano(input('plano (mensal, trimestral, semestral, anual): '))

            if(plano == 'm' or plano == 'mensal'):
                plano = PlanoMensal(mensalidade, data)

            elif(plano == 't' or plano == 'trimestral'):
                plano = PlanoTrimestral(mensalidade, data)
            
            elif(plano == 's' or plano == 'semestral'):
                plano = PlanoSemestral(mensalidade, data)
            
            else:
                plano = PlanoAnual(mensalidade, data)

            clientes[cpf] = Aluno(nome, cpf, plano)

            print('\nAluno registrado!')

        case 2:
            print('\n')
            
        case 3:
            print('\nBusca de informações do aluno por CPF')
            busca = int(input('Digite o CPF do aluno: '))
            cliente = clientes.get(busca, 'erro')

            if(cliente != 'erro'):
                print(f'\nNome: {cliente.get_nome()}')
                print(f'Plano: {cliente.plano.get_plano()}')
                print(f'Ficha de treino: {cliente.ficha.ficha_treino()}')

        case 4:
            print('\n')
        case 5:
            print('\nDesligando sistema')
            break
        case _:
            opcao = input('\nOpção inválida! Tente novamente: ')