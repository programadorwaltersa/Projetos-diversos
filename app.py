nome = input("Digite o nome: ")
idade = input("Digite a idade: ")
peso = input("Digite o peso: ")
altura = input("Digite a altura: ")
testeAluno = 12


idade_int = int(idade)
# Convertendo a o valor string de peso para float
peso_float = float(peso)
altura_float = float(altura)
# Calculando o IMC
altura_ao_quadrado = altura_float * altura_float
imc = peso_float / altura_ao_quadrado

print("Nome: ", nome)
print("Idade: ", idade_int)
print("Peso: ", peso_float)
print("Altura: ", altura_float)
print("O IMC é: ", imc)
type(idade)
print(type(idade))
type(peso)
print(type(peso))



 