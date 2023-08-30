from student_class import Students
from school_class import School
from scholarship_class import Scholarship
from instructor_class import Instructor


clientes = []
clientes.append(School("proprietária", "Ana", 13, 123456, 5552727))
clientes.append(Students("Aluno", "Bia", 23, 123456, 5552727, "Zuila", "Curso01", 150))
clientes.append(Students("Aluno", "Clara", 33, 123456, 5552727, "Yolli", "Curso02", 150,))
clientes.append(Students("Aluno", "Dani", 43, 123456, 5552727, "Xuxa", "Curso03", 150,))
clientes.append(Scholarship("Aluno", "Elga", 53, 123456, 5552727, "Wendy", "Curso01", 150, 25))
clientes.append(Scholarship("Aluno", "Fabi", 63, 123456, 5552727, "Vilma", "Curso03", 150, 10))
clientes.append(Instructor( "Instrutor", "Guigui", 73, 123456, 5552727, "Curso02", 300))
clientes.append(Instructor( "Instrutor", "Hera", 63, 123456, 5552727, "Curso03", 300))

list_curso = ["Curso01", "Curso02", "Curso03"]
def sel_curso():
    lista = list()
    Flag = False
    for i in list_curso:
        
        while Flag == False:
            elemento = input(f"Deseja matricular em {i}: (s ou n)").lower()
            
            if elemento == 's':
                lista.append(i)
                Flag = True
            elif elemento == 'n':
                Flag = True
            else:
                print('Opção invalida!')
                
                
    print(lista)    
    print(f'Matricula realizada em {lista}')
    return lista



#def
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
            
            if b == 'n':
                clientes.append(Students(lista[0], lista[1],int(lista[2]),lista[3],lista[4],lista[5],lista[6],int(lista[7])))
                Flage = True
            else:
                print('Opção Invalida!')
        break
            

    elif n == 'instrutor' or n == '1':
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
        print('Opção invalida!')
        

