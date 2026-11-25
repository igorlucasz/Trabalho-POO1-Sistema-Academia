from datetime import datetime
from zoneinfo import ZoneInfo
import time

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
        treino_inicial = treino_inicial.strip().lower()
        if(not treino_inicial):
            self.exercicios = []

        else:
            self.exercicios = treino_inicial.split(',')

            for i in range(len(self.exercicios)):
                self.exercicios[i] = self.exercicios[i].strip().capitalize()
    
    def ficha_treino(self):
        return self.exercicios

    def adicionar_exercicio(self, exercicio):
        self.exercicios.append(exercicio.strip().lower().capitalize())

    def remover_exercicio(self, indice_exercicio):
        self.exercicios.pop(indice_exercicio)

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
 
def verifica_inteiro(x): #verificação de números INTEIROS
    if(x.isdigit()):
        return x

    else:
        nova_resposta = input('Valor inválido! Digite um número válido: ')
        return verifica_inteiro(nova_resposta)

def verifica_plano(x):
    x = x.lower()
    if(x != 'm' and x != 'mensal' and x != 't' and x != 'trimestral' and x != 's' and x != 'semestral' and x != 'a' and x != 'anual'):
        nova_resposta = input('Plano inválido! Digite novamente: ')
        return verifica_plano(nova_resposta)
    else:
        return x

def verifica_cpf(x):
    if(x.isdigit() and len(x) == 11):
        return x

    else:
        nova_resposta = input('CPF inválido! Digite novamente: ')
        return verifica_cpf(nova_resposta)

def verifica_cadastro(x,dic):
    if(x in dic):
        return False

    else:
        return True

def consulta_ficha_de_treino(x,string):
    lista = x.ficha.ficha_treino()
    tamanho = len(lista)
    print(f'\n{string}') 

    if(tamanho == 0):
        print(f'Não criada.\n')

    else:
        for i in range(tamanho):
            print(f'[{i + 1}] {lista[i]}')

def verifica_indices(indices):
    for i in indices:
        if(i.isdigit()):
            num = True
        else:
            num = False
            break
    if num == True:
        indices = list(map(int, indices))
        if len(indices) != remover:
            indices = verifica_indices(input("Quantia de índices incorreta, tente novamente: ").replace(" ", "").split(','))
        for indice in indices:
            if not (0 < indice <= len(cliente.ficha.exercicios)):
                indices = verifica_indices(input("Índices inválidos, tente novamente: ").replace(" ", "").split(','))
                break
    else:
        indices = verifica_indices(input("Índices só podem ser números, tente novamente: ").replace(" ", "").split(','))  
    return indices

clientes = {}
mensalidade = 200

while(True):
    print('\n------------------------ Sistema Academia POO (Performance Orientada a Objetivos)  ------------------------')

    print('\nOpções:')
    print('1) Registrar aluno')
    print('2) Editar planilha de treino')
    print('3) Verificar aluno')
    print('4) Desligar sistema')
    opcao = input('\nDigite a opção desejada: ')

    match opcao:
        case '1':
            print('\nDigite as informações necessárias')
            data = str(datetime.now(ZoneInfo("America/Sao_Paulo")).date())
            nome = input('\nNome: ').title()
            cpf = verifica_cpf(input('CPF: '))
            if(verifica_cadastro(cpf, clientes) == False):
                print('\nAluno já cadastrado')
                time.sleep(1.5)
                continue
            plano = verifica_plano(input('Plano (mensal, trimestral, semestral, anual): '))
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
            time.sleep(1.5)

        case '2':
            print('\nEdição da Planilha de Treino')
            busca = verifica_cpf(input('Digite o CPF do aluno selecionado: '))
            cliente = clientes.get(busca,'erro')

            if(cliente != 'erro'):
                print(f'\nAluno selecionado: {cliente.nome}')
                consulta_ficha_de_treino(cliente,'Ficha de Treino Atual: ')

                time.sleep(1.5)

                adicionar = int(verifica_inteiro(input('Insira quantos exercícios deseja adicionar: ')))
                if adicionar > 0:
                    for i in range(adicionar):
                                        cliente.ficha.adicionar_exercicio(input(f'Digite o {i + 1}° exercício que deseja adicionar: '))
                    consulta_ficha_de_treino(cliente,'Ficha de Treino Atualizada: ')
                    time.sleep(1)
                elif adicionar < 0:
                    adicionar = int(verifica_inteiro(input('Valor inválido. Insira quantos exercícios deseja adicionar: ')))
                
                remover = int(verifica_inteiro(input('Quantos exercícios deseja remover: ')))
                while remover > len(cliente.ficha.ficha_treino()) or remover < 0:
                    remover = int(verifica_inteiro(input('Quantidade inválida. Insira quantos exercícios deseja remover: ')))
                if remover > 0:
                    indices_exercicios = verifica_indices(input("Insira o índice dos números que você deseja remover: ").replace(" ", "").split(','))
                    indices_exercicios.sort(reverse = True)
                    for i in indices_exercicios:
                        cliente.ficha.remover_exercicio(i - 1)
                consulta_ficha_de_treino(cliente, 'Ficha de Treino Atualizada: ')

                time.sleep(1.5)

            else:
                print('\nCPF não cadastrado.')
                time.sleep(1.5)
            
        case '3':
            print('\nBusca de informações do aluno por CPF')
            busca = verifica_cpf(input('Digite o CPF do aluno: '))
            cliente = clientes.get(busca, 'erro')

            if(cliente != 'erro'):
                print(f'\nNome: {cliente.get_nome()}')
                print(f'Plano: {cliente.plano.get_plano()}')
                print(f'Mensalidade: R$ {cliente.plano.calcular_mensalidade():.2f}')
                print(f'Data de vencimento do plano: {cliente.plano.vencimento()}', end = '')
                consulta_ficha_de_treino(cliente, f'Ficha de Treino - {cliente.get_nome()}')
                time.sleep(4)

            else:
                print('\nCPF não cadastrado.')
                time.sleep(1.5)

        case '4':
            print('\nDesligando sistema\n')
            break

        case _:
            print('\nOpção inválida!')
            time.sleep(1.5)