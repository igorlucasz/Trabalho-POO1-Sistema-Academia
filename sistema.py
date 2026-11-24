from datetime import datetime
from zoneinfo import ZoneInfo

class Aluno:
    def __init__(self, nome, cpf, plano, treino_inicial):
        self.nome = nome
        self.cpf = cpf
        self.plano = plano
        self.ficha = FichaDeTreino(treino_inicial)

    def get_nome(self):
        return self.nome

class FichaDeTreino:
    def __init__(self, treino_inicial):
        if(not treino_inicial.strip()):
            self.exercicios = []

        else:
            self.exercicios = treino_inicial.split(',')
    
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

def verifica_cpf(x):
    if(x.isdigit() and len(x) == 11):
        return int(x)

    else:
        nova_resposta = input('CPF inválido! Digite novamente: ')
        return verifica_cpf(nova_resposta)

def verifica_cadastro(x,dic):
    if(x in dic):
        return False

    else:
        return True


clientes = {}
mensalidade = 200
data = str(datetime.now(ZoneInfo("America/Sao_Paulo")).date())

while(True):
    print('\n------------------------ Sistema Academia POO (Performance Orientada a Objetivos)  ------------------------')

    print('\nOpções:')
    print('1) Registrar aluno')
    print('2) Editar planilha de treino')
    print('3) Verificar aluno')
    print('4) Sair do sistema')
    opcao = input('\nDigite a opção desejada: ')

    match opcao:
        case '1':
            print('\nDigite as informações necessárias')
            nome = input('\nNome: ')
            cpf = verifica_cpf(input('CPF: '))
            if(verifica_cadastro(cpf, clientes) == False):
                print('\nAluno já cadastrado')
                continue
            plano = verifica_plano(input('Plano (mensal, trimestral, semestral, anual): ').lower())
            treino_inicial = input('Treino inicial do aluno (se houver), separado por vírgulas: ')

            if(plano == 'm' or plano == 'mensal'):
                plano = PlanoMensal(mensalidade, data)

            elif(plano == 't' or plano == 'trimestral'):
                plano = PlanoTrimestral(mensalidade, data)
            
            elif(plano == 's' or plano == 'semestral'):
                plano = PlanoSemestral(mensalidade, data)
            
            else:
                plano = PlanoAnual(mensalidade, data)

            clientes[cpf] = Aluno(nome, cpf, plano, treino_inicial)

            print('\nAluno registrado!')

        case '2':
            print('\nEdição da Planilha de Treino')
            busca = verifica_cpf(input('Digite o CPF do aluno selecionado: '))
            cliente = clientes.get(busca,'erro')

            if(cliente != 'erro'):
                print(f'Ficha de treino do aluno: {cliente.ficha.ficha_treino()}')
                adicionar = int(input('Quantos exercícios deseja adicionar: '))

                for i in range(adicionar):
                    cliente.ficha.adicionar_exercicio(input('Digite o exercício que deseja adicionar: '))

                remover = int(input('Quantos exercícios deseja remover: '))

                for i in range(remover):
                    print('') #faz ai DAVI VACILÃO

            else:
                print('\nAluno não cadastrado.')
            
        case '3':
            print('\nBusca de informações do aluno por CPF')
            busca = verifica_cpf(input('Digite o CPF do aluno: '))
            cliente = clientes.get(busca, 'erro')

            if(cliente != 'erro'):
                print(f'\nNome: {cliente.get_nome()}')
                print(f'Plano: {cliente.plano.get_plano()}')
                print(f'Data de vencimento do plano: {cliente.plano.vencimento()}')
                print(f'Ficha de treino: {cliente.ficha.ficha_treino()}')

            else:
                print('\nAluno não cadastrado.')

        case '4':
            print('\nDesligando sistema')
            break

        case _:
            print('\nOpção inválida!')