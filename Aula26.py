#  Você está construindo um sistema de gerenciamento de contatos. Crie um programa que realize as seguintes tarefas:

#  a) Peça ao usuário para digitar seu nome completo.
nome_completo = input("Digite seu nome completo: ")
print("Olá, " + nome_completo)

#  b) Concatene “Olá,” com o nome fornecido e exiba o resultado.
nome_completo = input("Digite seu nome completo: ")
print("Olá, " + nome_completo)

#  c) Conte quantos caracteres existem no nome completo digitado e exiba o resultado.
print("O nome completo tem", len(nome_completo), "caracteres.")
#  d) Peça ao usuário para digitar um sobrenome para procurar na string do nome completo.
print("O nome completo tem", len(nome_completo), "caracteres.")

#  e) Verifique se o sobrenome fornecido está presente no nome completo e exiba uma mensagem apropriada.
sobrenome = input("Digite um sobrenome para procurar: ")
if sobrenome in nome_completo:
  print("O sobrenome foi encontrado no nome completo.")
else:
  print("O sobrenome não foi encontrado no nome completo.")

#  f) Exiba o nome completo em letras maiúsculas.
print(nome_completo.upper())

#  g) Substitua todas as ocorrências da vogal “a” na string do nome completo pelo caractere ‘4’ e exiba o resultado
nome_completo_modificado = nome_completo.replace("a", "4")
print(nome_completo_modificado)
