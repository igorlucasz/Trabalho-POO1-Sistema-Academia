# Trabalho-POO1-Sistema-Academia
Trabalho para a matéria de POO na faculdade sobre um sistema de academia

# Requisitos:
- uso de Estruturas de Seleção/Repetição;
- uso de Lista e/ou ListaComposta e/ou Matriz e/ou Dicionário;
- exemplo/uso de Instanciação;
- exemplo/uso de Herança;
- exemplo/uso de Polimorfismo;
- exemplo/uso de Agregação ou Composição;
- manipulação de uma lista de objetos (ações: inserir, alterar, consultar e excluir)
- implementar um MENU apresentando as funcionalidades do programa

# Organização:
O projeto consiste em um sistema de gerenciamento dos clientes de uma academia. 

Dicionários:

- clientes[nome]

Classes:

- Plano(mensalidade, data_vencimento)
- PlanoMensal(mensalidade, data_vencimento) — herda de Plano
- PlanoTrimestral(mensalidade, data_vencimento) — herda de Plano, 10% de desconto
- PlanoSemestral(mensalidade, data_vencimento) — herda de Plano, 15% de desconto
- PlanoAnual(mensalidade, data_vencimento) — herda de Plano, 20% de desconto
- FichaDeTreino(exercicios) — composta dentro de Aluno
- Aluno(nome, cpf, plano, ficha) — recebe Plano por agregação, cria FichaDeTreino por composição

Polimorfismo:

- calcular_mensalidade() sobrescrito em cada subclasse de Plano
