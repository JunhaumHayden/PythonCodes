#conta_historico.py
#exemplo composicao

import datetime

class Historico():
    def __init__(self):
        self.data_matricula = datetime.datetime.today()
        self.notas=[]
        
    def imprime(self):
        print("data Matricula: {}".format(self.data_matricula))
        print("historico no sistema: ")
        for t in self.notas:
            print("-", t)
            
class Conta():
    def __init__(self, id, cliente):
        self.id = id
        self.cliente = cliente
        self.historico = Historico()

    #def __del__(self):
    #    del self.id
    #    del self.cliente
    #    del self.historico
    
        #rint("Matricula Encerrada")
    
    def get_curso(self):
        return self.cliente.curso.curso    
    def set_curso(self,curso):
        self.cliente.curso.curso = curso
        
        
    def imprime_info_financeiras(self):
         
         print("Informacoes Financeiras: ")
         #print("Data da Matricula: {}".format(Historico.imprime(self)))
         if self.cliente.tipo == "Instrutor":
             print(f'Profrssor: {self.cliente.nome}')
             print(f'Mistra: {self.cliente.get_curso()} Salario: {self.cliente.get_salario()}')
         elif self.cliente.tipo == "Aluno":
             print(f'Nome: {self.cliente.nome}, Nome do responsavel: {self.cliente.nome_resp}')
             #print(f'Curso: {self.get_curso()} valor: {self.get_mensalidade()}')
             print(f'Aluno com desconte de {self.cliente.get_desconto()}')
         else:
             print(f'Nome: {self.cliente.nome}, Tipo: {self.cliente.tipo}')
             
         self.historico.notas.append("Consulta Financeira realizada em : {}".format(datetime.datetime.today()))  
             
         
         
         
    def imprime_info_cadastral(self):
         print("Informacoes Cadastrais: ")
         self.historico.imprime()
         print(f'{self.cliente.tipo}')
         print(f'{self.cliente.nome}, Nome do responsavel: {self.cliente.nome_resp}')
         print(f'CPF: {self.cliente.cpf}, Telefome: {self.cliente.fone}')
         print(f'{self.cliente.get_curso()}')
         print(f'Nota da avaliacao 01: {self.get_nota01()} \nNota da avaliacao 02: {self.get_nota02()}')
         n1 = self.get_nota01
         n2 = self.get_nota02
         #media = ( float(n10)+ float(n20)) / 2
         #print(f'Media de: {media}')
         self.historico.notas.append("Consulta Cadastral realizada em : {}".format(datetime.datetime.today()))

         
    def get_nota01(self):
        return self.cliente.curso.nota01
    def set_nota01(self,curso):
        self.cliente.curso.nota01 = curso
        print(f'Alterado para {curso}')
       

    def get_nota02(self):
        return self.cliente.curso.nota02
    def set_nota02(self,curso):
        self.cliente.curso.nota02 = curso
        print(f'Alterado para {curso}')
       

    def get_valor(self):
        return self.cliente.curso.valor    
    def set_valor(self,valor):
        self.cliente.curso.valor = valor
        
    
    def set_removeCurso(self,curso):
        del dict_curso[curso]  

      
        
    
    
            