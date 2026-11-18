class Clientes:
    def __init__(self, nome, nascimento, idade, cpf):
        self.nome = nome
        self.nascimento = nascimento
        self.idade = idade
        self.cpf = cpf

    def get_nome(self):
        return self.nome

