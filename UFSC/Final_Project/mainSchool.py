from student_class import Students
from school_class import School
from scholarship_class import Scholarship
from instructor_class import Instructor
from Courses_class import Courses


# Exemplo de uso
clientes = []
clientes.append(School("proprietária", "Ana", 13, 123456, 5552727))
clientes.append(Students("Aluno", "Bia", 23, 123456, 5552727, "Zuila", "Curso01", 150))
clientes.append(Students("Aluno", "Clara", 33, 123456, 5552727, "Yolli", "Curso02", 150,))
clientes.append(Students("Aluno", "Dani", 43, 123456, 5552727, "Xuxa", "Curso03", 150,))
clientes.append(Scholarship("Aluno", "Elga", 53, 123456, 5552727, "Wendy", "Curso01", 150, 25))
clientes.append(Scholarship("Aluno", "Fabi", 63, 123456, 5552727, "Vilma", "Curso03", 150, 10))
clientes.append(Instructor( "Instrutor", "Guigui", 73, 123456, 5552727, "Curso02", 300))
clientes.append(Instructor( "Instrutor", "Hera", 63, 123456, 5552727, "Curso03", 300))

list_curso = []
list_curso.append(Courses('curso01', 200))
list_curso.append(Courses('curso02',150))
list_curso.append(Courses('curso01',100))


def sel_curso():
    lista = []
    for i in range(len(list_curso)):
        elemento = input(f"Deseja matricular em {list_curso[i].curso}? (s ou n)").lower()
        if elemento == 's':
            lista.append(list_curso[i].curso)
            lista.append(list_curso[i].valor)
            
            break
    print(f'Matricula realizada em {list_curso[i].curso} valor de {list_curso[i].valor} ')
    return lista



def cadastro():
    lista = list()
    inst = ["o nome", "a idade", "o cpf", "o telefone", "curso", "o salario"]
    alun = ['o nome', 'a idade', 'o cpf', 'o telefone', 'o nome do responsavel', 'curso', 'O valor da mensalidade']

    while True:
        n = input(' tipo: 1 - aluno, 2 - Instrutor: ').lower()

        
        if n == 'aluno' or n == '1':
            lista.append('Aluno')
            
            for i in alun:
                print(i)
                i == 'curso'
                if i == 'curso':
                    c = sel_curso()
                    lista.append(c[0])
                    lista.append(c[1])
                elif i == 'O valor da mensalidade':
                    print(c[1])
                else:
                    elemento = input(f"Digite {i}: ")
                    lista.append(elemento)
            
            Flage = False
            while Flage == False:
                b = input('Aluno Bolsista? (s ou n)').lower()
                if b == 's':
                    valor = input('Qual a porcentagem? ')
                    lista.append(valor)
                    clientes.append(Scholarship(lista[0],lista[1],int(lista[2]),lista[3],lista[4],lista[5],lista[6],int(lista[7]),int(lista[8])))
                    Flage = True
                
                elif b == 'n':
                    clientes.append(Students(lista[0], lista[1],int(lista[2]),lista[3],lista[4],lista[5],lista[6],int(lista[7])))
                    Flage = True
                else:
                    
                    print('Opção Invalida!')
            break
                

        elif n == 'instrutor' or n == '2':
            lista.append('Instrutor')
            
            for i in inst:
                print(i)
                i == 'curso'
                if i == 'curso':
                    c = sel_curso()
                    lista.append(c[0])
                else:
                    elemento = input(f"Digite {i}: ")
                    lista.append(elemento)
            clientes.append(Instructor(lista[0], lista[1],int(lista[2]),lista[3],lista[4],lista[5],int(lista[6])))
            break
        else:
            
            print('Opção invalida, tente novamente!')
            

#Funcao teste de ID existente
def test():
    print( )
    print( )
    temp = int(input('Informe o Id: '))
    while temp >= len(clientes):
        print( )
        print( )
        print("="*30)
        print('ID Invalido. Tente Novamente')
        print("="*30)
        print( )
        temp = int(input('Informe o Id: '))
    else:
        return temp

def conta_curso_inst(clientes):
    cont_curso = []
    curs01 = 0
    curs03 = 0
    curs02 = 0
    
    for cliente in clientes:
        if cliente.get_tipo() == 'Instrutor' and cliente.get_curso() == 'Curso01':
            curs01 += 1
        if cliente.get_tipo() == 'Instrutor' and cliente.get_curso() == 'Curso02':
            curs02 += 1
        if cliente.get_tipo() == 'Instrutor' and cliente.get_curso() == 'Curso03':
            curs03 += 1    
    cont_curso.append(curs01)
    cont_curso.append(curs02)
    cont_curso.append(curs03)
    return cont_curso

def conta_curso_aluno(clientes):
    cont_curso = []
    curs01 = 0
    curs03 = 0
    curs02 = 0
    
    for cliente in clientes:

        if cliente.get_tipo() == 'Aluno' and cliente.get_curso() == 'Curso01':
            curs01 += 1
        if cliente.get_tipo() == 'Aluno' and cliente.get_curso() == 'Curso02':
            curs02 += 1
        if cliente.get_tipo() == 'Aluno' and cliente.get_curso() == 'Curso03':
            curs03 += 1    
    cont_curso.append(curs01)
    cont_curso.append(curs02)
    cont_curso.append(curs03)
    return cont_curso

#Menu de interacao
while True: 

    print("="*30)
    print("    Menu principal")
    print("="*30)
    print( )
    n = input(' 1 - Cadastro \n 2 - Imprime inf \n 3 - Consulta Desconto \n 4 - Consulta Mensalidade \n 5 - Lotação \n 0 - Encerrar \n Opção: ')
    for _ in range(7):
        print()

    if n == '0':
        print("="*30)
        print("    Programa Encerrado")
        print("="*30)
        break
    elif n == '1':
        
        print("="*30)
        print("  Cadastro")
        print("="*30)
        cad = cadastro()
        print("="*30)
        print( )
        print( )
    
    elif n == '2':
        for _ in range(4):
            print()
        print("="*30)
        print("    Consulta Cliente")
        print("="*30)
        print( )
        print( )
        t = input('deseja imprimir a lista de clientes? (S ou N): ')
        print( )
        print( )
        print(f'Opção escolhida: {t}')
        print( )
        print( )
        if t == 's':
            print("="*30)
            print("  Lista de Cliente")
            print("="*30)

            for i in range(len(clientes)):
                    print("="*30)
                    print(f'ID: {i}')
                    print("="*30)
                    
                    clientes[i].__str__()
        else:
            c = test()
            print("="*30)
            print("  Consulta por ID")
            print("="*30)
            print("="*30)
            print(f"  ID {c}")
            print("="*30)
            clientes[c].__str__()
            print( )
            print( )
            
            
          # Verificar se o cliente possui Desconto          
    elif n == '3':
        c = test()
        restricao = clientes[c].get_desconto()
        print("="*30)
        print(" Desconto")
        print("="*30)
        print( )
        print( )
        print(f"O desconto de {clientes[c].get_nome()} é de : {restricao} % ")
        print( )
        print( )
            

       # Calcular mensalidade do cliente
    elif n == '4':
        c = test()
        mensalidade = clientes[c].get_mensalidade()
        print("="*30)
        print(" Calcular Mensalidade")
        print("="*30)
        print( )
        print( )
        print("Mensalidade:", mensalidade)
        print(f"  A mensalidade é de {mensalidade} Reais \n  Aluno com desconto de {clientes[c].get_desconto()} %")
        print( )
        print( )

     # Encontrar o cliente mais idoso
    elif n == '5':
        print("="*30)
        print(" Lotação por curso")
        print("="*30)

        cursos = conta_curso_aluno(clientes)
        print("Alunos x Curso:")
        print(f'Curso01: {cursos[0]}')
        print(f'Curso02: {cursos[1]}')
        print(f'Curso03: {cursos[2]}')
        print( )
        print( )
        cursos = conta_curso_inst(clientes)
        print("Instrutor x Curso:")
        print(f'Curso01: {cursos[0]}')
        print(f'Curso02: {cursos[1]}')
        print(f'Curso03: {cursos[2]}')
    else:
        print('tente novamente')