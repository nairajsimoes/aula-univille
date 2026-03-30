from datetime import date 
 
# Exercício 1 - Peça o nome e exiba uma saudação 
nome = input("Digite seu nome: ") 
print(f"Olá, {nome}! Bem-vindo(a) à aula de Python!")

# Exercício 2 - Peça um Número e Mostre o Dobro 
numero = int(input('Digite um número para ver quanto é o dobro: '))
print(f'O dobro de {numero} é {numero * 2}!')

# Exercício 3 - Peça Dois Números e Mostre a Soma
soma = int(input(f'Digite um número: ')) 
soma2 = int(input('Digite outro número: '))
print(f'A soma de {soma} + {soma2} é {soma + soma2}!')

# Exercício 4 - Calcule a Idade a Partir do Ano de Nascimento
ano_atual = date.today().year
ano_nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - ano_nascimento
print(f'Você tem {idade} anos!')

# Exercício 5 - Calcule o Aumento de Salário (10%)
salario = float(input("Digite seu salário atual:"))
aumento = salario*0.10 
novo_salario = salario + aumento
print(f"Salário atual: R$ {salario:.2f} → Novo salário: R$ {novo_salario:.2f}")

# Exercício 6 - Converta Celsius para Fahrenheit
celsius = float(input(f'Digite a temperatura em Celsius:'))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura {celsius}° é igual a {fahrenheit}F!")

# Exercício 7 - Mostre Dados Completos: Nome, Idade e Cidade
nome = input(f'Vamos fazer seu cadastro! Comece botando seu nome:')
idade = int(input(f'Agora digite sua idade:'))
cidade = input(f'Por último, nos diga sua cidade:')
print(f'Informações de cadastro: Nome: {nome} | Idade: {idade} | Cidade: {cidade}')

# Exercício 8 - Faça Todas as Operações Matemáticas
a = int(input(f'Digite um número inteiro para as operações matemáticas:'))
b = int(input(f'Digite outro número inteiro:'))
print(f'A soma dos dois números {a} + {b} é igual a {a+b}')
print(f'A subtração dos dois números {a} - {b} é igual a {a-b}')
print(f'A multiplicação dos dois números {a} * {b} é igual a {a*b}')
print(f'A divisão dos dois números {a} / {b} é igual a {a/b}')
print(f'O resto de dois números {a} % {b} é igual a {a%b}')

# Exercício 9 - Calcule o Salário por Horas Trabalhadas

# Exercício 10 - Converta Reais para Dólares