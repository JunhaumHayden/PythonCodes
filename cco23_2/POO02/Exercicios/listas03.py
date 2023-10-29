#Item06 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a
#média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
import random

def calcular_media(notas):
    return sum(notas) / len(notas)

def gerar_notas_aleatorias(num_alunos):
    medias = []
    notas = []
    for i in range(num_alunos):
        #nota = []
        nota = [random.uniform(0, 10) for _ in range(4)]
        media = calcular_media(nota)
        medias.append(media)
        notas.append(nota) 
    return notas, medias

def gerar_notas_manual(num_alunos):
    medias = []
    notas = []
    for i in range(num_alunos):
        nota = []
        for j in range(4):
            ava = float(input(f"Digite a nota {j + 1} do aluno {i + 1}: "))
            nota.append(ava)
        
        media = calcular_media(notas)
        medias.append(media)
        notas.append(nota)
    return notas, medias


#a função ler_dados é responsável por ler as idades e alturas dos alunos, armazenando-as em vetores separados. Em seguida, na função main, percorremos os vetores na ordem inversa (do último ao primeiro elemento) e imprimimos a idade e altura correspondentes.

def ler_dados(num_alunos):
    idades = []
    alturas = []
    for i in range(num_alunos):
        idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
        altura = float(input(f"Digite a altura da pessoa {i + 1} (em metros): "))
        idades.append(idade)
        alturas.append(altura)
    return idades, alturas


#Funcao auxiliar para apresentacao dos menus
def printing(msg):
    print("="*30)
    print(f"{msg}")
    print("="*30)
    print( )

# Função principal
def main():
    num_alunos = 10
    medias = []
    notas = []
    printing("Escolha uma opção:")
    print("1. Informar os notas manualmente")
    print("2. Gerar notas automaticamente")
    
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        notas, medias = gerar_notas_manual(num_alunos)
    elif opcao == 2:
        notas, medias = gerar_notas_aleatorias(num_alunos)
    else:
        print("Opção inválida. Encerrando o programa.")
        return

    
        
    
    # Contar o número de alunos com média maior ou igual a 7.0
    printing('Alunos aprovados')
    alunos_aprovados = sum(1 for media in medias if media >= 7.0)
    
    for i in len(notas):
        for j in len(notas[i]):
            print(f'nota {j +1} do aluno {i +1}')
            print(j)


    print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")

   
    printing('Apresentando\n idade e altura \nna ordem inversa')
    idades, alturas = ler_dados()

    print("\nDados na ordem inversa à ordem lida:")

    for i in range(4, -1, -1):
        print(f"Aluno {i + 1} - Idade: {idades[i]} anos, Altura: {alturas[i]:.2f} metros")

num_alunos = 4
medias = []
notas = []
if __name__ == "__main__":
    #main()
   
    printing("Escolha uma opção:")
    print("1. Informar os notas manualmente")
    print("2. Gerar notas automaticamente")
    
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        notas, medias = gerar_notas_manual(num_alunos)
    elif opcao == 2:
        notas, medias = gerar_notas_aleatorias(num_alunos)
    else:
        print("Opção inválida. Encerrando o programa.")
    

    # Contar o número de alunos com média maior ou igual a 7.0
    printing('Alunos aprovados')
    alunos_aprovados = sum(1 for media in medias if media >= 7.0)
    
    for i in range(len(notas)):
        for j in range(len(notas[i])):
            print(f'nota {j +1} do aluno {i +1}')
            print(f'{notas[i][j]:.2f}')


    print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")

   
    printing('Apresentando\n idade e altura \nna ordem inversa')
    idades, alturas = ler_dados(num_alunos)

    print("\nDados na ordem inversa à ordem lida:")

    for i in range(len(idades), -1, -1):
        print(f"Aluno {i + 1} - Idade: {idades[i]} anos, Altura: {alturas[i]:.2f} metros")
        for j in range(len(notas[i])):
            print(f'nota {j +1} do aluno {i +1}')
            print(f'{notas[i][j]:.2f}')