from datetime import date 

nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Bem-vindo(a) à aula de Python!")

numero = int(input('Digite um número para ver quanto é o dobro: '))
print(f'O dobro de {numero} é {numero * 2}!')

soma = int(input(f'Digite um número: ')) 
soma2 = int(input('Digite outro número: '))
print(f'A soma de {soma} + {soma2} é {soma + soma2}!')

ano_atual = date.today().year
ano_nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - ano_nascimento
print(f'Você tem {idade} anos!')