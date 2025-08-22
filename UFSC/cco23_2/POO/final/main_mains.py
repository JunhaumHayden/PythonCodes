##Aluno: Carlos Benedito Hayden de Albuquerque Junior
##matricula: 23100455
##Helcio Valentim de Andrade Neto (23100476)



from class_student import Students
from class_school import School
from class_scholarship import Scholarship
from class_instructor import Instructor
from class_courses import Courses
from class_historico import Conta,Historico

list_curso = []
list_curso.append(Courses('Matemática', 20,0,0))
list_curso.append(Courses('Português', 30,0,0))
list_curso.append(Courses('Física'   , 40,0,0))
list_curso.append(Courses('Química'  , 50,0,0))
list_curso.append(Courses('Biologia' , 60,0,0))

# Exemplo de uso
clientes = []
clientes.append(School("proprietária", "Ana", 13, 123456, 5552727))
clientes.append(Students("Aluno", "Bia", 23, 123456, 5552727, "Zuila", list_curso[0], 150))
clientes.append(Students("Aluno", "Clara", 33, 123456, 5552727, "Yolli",list_curso[1], 150,))
clientes.append(Students("Aluno", "Dani", 43, 123456, 5552727, "Xuxa", list_curso[2], 150,))
clientes.append(Scholarship("Aluno", "Elga", 53, 123456, 5552727, "Wendy", list_curso[3], 150, 25))
clientes.append(Scholarship("Aluno", "Fabi", 63, 123456, 5552727, "Vilma", list_curso[4], 150, 10))
clientes.append(Instructor( "Instrutor", "Guigui", 73, 123456, 5552727, list_curso[1], 300))
clientes.append(Instructor( "Instrutor", "Hera", 63, 123456, 5552727, list_curso[2], 300))



lista_historico = []

lista_historico.append(Conta(0, clientes[0]))
lista_historico.append(Conta(1, clientes[1]))
lista_historico.append(Conta(2, clientes[2]))
lista_historico.append(Conta(3, clientes[3]))
lista_historico.append(Conta(4, clientes[4]))
lista_historico.append(Conta(5, clientes[5]))
lista_historico.append(Conta(6, clientes[6]))
lista_historico.append(Conta(7, clientes[7]))


## Funcoes auxiliares

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

#Funcao de selecao de curso
def sel_curso():
    lista = []
    for i in range(len(list_curso)):
        elemento = input(f"Seleciona {list_curso[i].curso}? (s ou n)").lower()
        if elemento == 's':
            lista.append(list_curso[i].curso)
            lista.append(list_curso[i].valor)
            lista.append(0)
            lista.append(0)
            
            break
    print(f'Matricula realizada em {list_curso[i].curso} valor de {list_curso[i].valor} ')
    return lista


#######Funcoes de alteracao de listas

def cadastro():
    lista = list()
    inst = ["o nome", "a idade", "o cpf", "o telefone", "curso", "o salario"]
    alun = ['o nome', 'a idade', 'o cpf', 'o telefone', 'o nome do responsavel', 'curso', 'O valor da mensalidade']

    while True:
        n = input(' tipo: 1 - aluno, 2 - Instrutor: ').lower()
        if n == 'aluno' or n == '1':
            lista.append('Aluno')
            
            for i in alun:
                if i == 'curso':
                    c = sel_curso()
                    lista.append(c)

                elif i == 'O valor da mensalidade':
                    lista.append(c[1])

                else:
                    elemento = input(f"Digite {i}: ")
                    lista.append(elemento)
            #print(lista)
            Flage = False
            while Flage == False:
                b = input('Aluno Bolsista? (s ou n)').lower()
                if b == 's':
                    valor = input('Qual a porcentagem? ')
                    lista.append(valor)
                    clientes.append(Scholarship(lista[0],lista[1],int(lista[2]),lista[3],lista[4],lista[5],lista[6],int(lista[7]),int(lista[8])))
                    lista_historico.append(Conta(len(clientes) - 1, clientes[len(clientes) - 1]))
                    Flage = True
                
                elif b == 'n':
                    clientes.append(Students(lista[0], lista[1],int(lista[2]),lista[3],lista[4],lista[5],lista[6],int(lista[7])))
                    lista_historico.append(Conta(len(clientes) - 1, clientes[len(clientes) - 1]))
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
            lista_historico.append(Conta(len(clientes) - 1, clientes[len(clientes) - 1]))
            break
        else:
            
            print('Opção invalida, tente novamente!')
            
            
def altera_curso():
    c = test()
    print("="*30)
    print(" Alterando Curso")
    print("="*30)
    print( )
    print( )
    curso  = sel_curso()
    lista_historico[c].set_curso(curso[0])
    print (f'Curso alterado para {lista_historico[c].get_curso()}')
    return
    

def altera_nota01():
    c = test()
    print("="*30)
    print("     Avaliações")
    print("="*30)
    print( )
    print( )
    lista_historico[c].set_nota01(input('Informe a nota para a avaliacao 01: '))
    print (f'Nota da avaliação 01 de {lista_historico[c].get_curso()} é de: {lista_historico[c].get_nota01()}')
    

def altera_nota02():
    c = test()
    print("="*30)
    print("     Avaliações")
    print("="*30)
    print( )
    print( )
    lista_historico[c].set_nota02(input('Informe a nota para a avaliacao 02: '))
    print (f'Nota da avaliação 02 de {lista_historico[c].get_curso()} é de: {lista_historico[c].get_nota02()}')
    
def altera_valor_mensal():
    c = test()
    print("="*30)
    print("  Alterar valor mensalidade")
    print("="*30)
    print( )
    print( )
    lista_historico[c].set_valor(input('Informe o valor da mensalidade:'))
    print (f'O valor da mensalidade de {lista_historico[c].cliente.nome} é de: {lista_historico[c].get_valor()}')
 
def encerra_matricula():
    c = test()
    clientes.pop(c)
    print("="*30)
    print("  Encerrar Matricula")
    print("="*30)
    print( )
    print( )
    ##lista_historico[c].__del__()
    
    
 
 
 
 
 
#######Funcoes opercacoes logicas 
def calc_desconto():
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
            
def cal_mensalidade():
    c = test()
    mensalidade = clientes[c].get_mensalidade()
    print("="*30)
    print(" Calcular Mensalidade")
    print("="*30)
    print( )
    print( )
    print("  Mensalidade:", mensalidade)
    print(f"  A mensalidade é de {mensalidade} Reais \n  Aluno com desconto de {clientes[c].get_desconto()} %")
    print( )
    print( )
    
def info_financeira():
    c = test()
    lista_historico[c].imprime_info_financeiras()
    
    
def info_cadastrais():
    c = test()
    lista_historico[c].imprime_info_cadastral()
    

def historico():
    c = test()
    print("\nImprimindo o histórico: ")
    lista_historico[c].historico.imprime()
    
    
    
def calcular_pagamentos():
    total_recebido = 0
    total_pagamentos = 0
    for a in range(len(clientes)):
        total_recebido += clientes[a].get_mensalidade()
        total_pagamentos += clientes[a].get_salario()
    print("="*30)
    print(" Pagamentos")
    print("="*30)
    print( )
    print(f'Ate {lista_historico[0].historico.data_matricula}')
    print(f'O toral recebido foi de: {float(total_recebido)} Reais')
    print(f'O toral de pagamentos foi de: {float(total_pagamentos)} Reais')
    print(f'A diferença é de: {float(total_recebido - total_pagamentos)} Reais')
    return
    

   
def conta_curso_aluno():
    
    Matematica = 0
    Portugues = 0
    Fisica = 0
    Biologia = 0
    Quimica = 0
    
    for a in range(len(clientes)):

        if clientes[a].get_tipo() == 'Aluno' and clientes[a].get_curso() == 'Matemática':
            Matematica += 1
        if clientes[a].get_tipo() == 'Aluno' and clientes[a].get_curso() == 'Português':
            Portugues += 1
        if clientes[a].get_tipo() == 'Aluno' and clientes[a].get_curso() == 'Física':
            Fisica += 1
        if clientes[a].get_tipo() == 'Aluno' and clientes[a].get_curso() == 'Química':
            Quimica += 1
        if clientes[a].get_tipo() == 'Aluno' and clientes[a].get_curso() == 'Biologia':
            Biologia += 1
    print("="*30)
    print(" Informacoes Administrativas")
    print("="*30)
    print( )      
    print(f'Alunos Matriculados em:')
    print(f'Matematica: {Matematica}')
    print(f'Portugues:  {Portugues}')
    print(f'Fisica:     {Fisica}')
    print(f'Biologia:   {Biologia}')
    print(f'Quimica:    {Quimica}')
    
    for a in range(len(clientes)):

        if clientes[a].get_tipo() == 'Instrutor' and clientes[a].get_curso() == 'Matemática':
            Matematica += 1
        if clientes[a].get_tipo() == 'Instrutor' and clientes[a].get_curso() == 'Português':
            Portugues += 1
        if clientes[a].get_tipo() == 'Instrutor' and clientes[a].get_curso() == 'Física':
            Fisica += 1
        if clientes[a].get_tipo() == 'Instrutor' and clientes[a].get_curso() == 'Química':
            Quimica += 1
        if clientes[a].get_tipo() == 'Instrutor' and clientes[a].get_curso() == 'Biologia':
            Biologia += 1
    print(f'Professores que lecionam:')
    print(f'Matematica: {Matematica}')
    print(f'Portugues:  {Portugues}')
    print(f'Fisica:     {Fisica}')
    print(f'Biologia:   {Biologia}')
    print(f'Quimica:    {Quimica}')
    


def info_financeira():
    c = test()
    lista_historico[c].imprime_info_financeiras()
    
    
def info_cadastrais():
    c = test()
    print("Data de matricula: ",lista_historico[0].historico.data_matricula)
    lista_historico[c].imprime_info_cadastral()
    

def historico(self):
    c = test()
    print("Data de matricula: ",lista_historico[i].historico.data_matricula)
    print("\nImprimindo o histórico: ")
    lista_historico[c].historico.imprime()
  
    




#Menu de interacao
while True: 
    pass
    print("="*30)
    print("    Menu principal")
    print("="*30)
    print( )
    n = input(' 1 - Dados de Cadastro \n 2 - Alteracao cadastro \n 3 - Alteracoes Financeiro \n 4 - Informacoes Administrativas \n 5 - Lotação \n 0 - Encerrar \n Opção: ')
    for _ in range(7):
        print()

    if n == '0':
        print("="*30)
        print("    Programa Encerrado")
        print("="*30)
        break
    elif n == '1':
        while True:
            print("="*30)
            print("    Menu Dados de Cadastro")
            print("="*30)
            print( )
            control = (input(' 1 - Cadastrar novo aluno ou instrutor \n 2- Cadastrar de notas \n 3 - Alterar curso \n 4 - Alterar mensalidade \n 5- Encerrar matricula \n 0 - volta \n: '))
            if control == '0':
                
                break
            elif control == '1':
                print("="*30)
                print("  Dados de Cadastro")
                print("="*30)
                cad = cadastro()
                print("="*30)
                print( )
                print( )
                
               
            elif control == '2':
                print("="*30)
                print("  Cadastrar de notas")
                print("="*30)
                while True:
                #Tratamento de excecao
                    try:
                        N = int, input('1 - 01 Avaliação\n 2 - 02 Avaliação\n : ')
                        break
                    except ValueError:
                        print("Entrada inválida. Certifique-se de fornecer os valores corretos.")
                if n == '1':
                    cad = ç()
                if n == '2':
                    cad = altera_nota02()
                print("="*30)
                print( )
                print( )
                
            elif control == '3':
                print("="*30)
                print("  Alterar curso")
                print("="*30)
                cad = altera_curso()
                print("="*30)
                print( )
                print( )
                
            elif control == '4':
                print("="*30)
                print("  Alterar mensalidade")
                print("="*30)
                cad = altera_valor_mensal()
                print("="*30)
                print( )
                print( )
                
            elif control == '5':
                print("="*30)
                print("  Alterar mensalidade")
                print("="*30)
                cad = encerra_matricula()
                print("="*30)
                print( )
                print( )
               
            else:
                print('tente outra vez')
            
    
    elif n == '2':
        while True:
            print()
            print()
            print("="*30)
            print("  Menu Consultas")
            print("="*30)
            print( )
            control = (input(' 1 - Informações Cadastrais \n 2 - Alteracao de notas \n 3 - Alterar curso \n 4 - Encerrar matricula \n 0 - volta \n: '))
            if control == '0':
                break
            
            elif control == '1':
                t = input('deseja imprimir a lista de clientes? (S ou N): ')
                print( )
                print( )
                print(f'Opção escolhida: {t}')
                print( )
                print( )
                if t == 's':
                    print("="*30)
                    print("  Lista de todos os Cliente")
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
                
               
            elif control == '2':
                print("="*30)
                print("  Cadastrar de notas")
                print("="*30)
                while True:
                #Tratamento de excecao
                    try:
                        N = int, input('1 - Alterar nota da Avaliação 02\n 2 - Alterar nota da Avaliação02\n : ')
                        break
                    except ValueError:
                        print("Entrada inválida. Certifique-se de fornecer os valores corretos.")
                if n == '1':
                    cad = altera_nota01()
                if n == '2':
                    cad = altera_nota02()
                print("="*30)
                print( )
                print( )
                
            elif control == '3':
                print("="*30)
                print("  Alterar curso")
                print("="*30)
                cad = altera_curso()
                print("="*30)
                print( )
                print( )
            
                
            elif control == '4':
                print("="*30)
                print("  Encerrar matricula")
                print("="*30)
                cad = encerra_matricula()
                print("="*30)
                print( )
                print( )
               
            else:
                print('tente outra vez')
        
            
            
          # menu financeiro         
    elif n == '3':
        while True:
            
            control = (input('1 - Informacoes cadastrais \n 2- Informacoes Financeiras \n 3 - Alterar mensalidade \n 4 - Calcular desconto \n 5 - Calcular mensalidade \n 0 - volta \n: '))
            if control == '0':
                break
            if control == '1':
                print("="*30)
                print("  Informacoes cadastrais")
                print("="*30)
                cad = info_cadastrais()
                print("="*30)
                print( )
                print( )
    
                
            elif control == '2':
                print("="*30)
                print("  info_financeira")
                print("="*30)
                cad = info_financeira()
                print("="*30)
                print( )
                print( )
                
                
            elif control == '3':
                print("="*30)
                print("  Alterar mensalidade")
                print("="*30)
                cad = altera_valor_mensal()
                print("="*30)
                print( )
                print( )
                
            elif control == '4':
                temp = calc_desconto()
                
            elif control == '5':
                temp = cal_mensalidade()
                
            else:
                print('tente outra vez')
            

       # Menu Administrativo
    elif n == '4':
       
        conta_curso_aluno()
        

     
    elif n == '5':
        print("="*30)
        print(" Lotação por curso")
        print("="*30)

        print("404 Page Not Found")
        print()
        print()
        print('The page youre looking for cant be found')
        print()
        print('a code 0x80244019 or as the message WU_E_PT_HTTP_STATUS_NOT_FOUND.')
       
        
            
            
            
            
