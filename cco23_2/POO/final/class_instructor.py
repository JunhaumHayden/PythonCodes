from class_school import School

class Instructor(School):
    """Classe de estudantes"""
    def __init__(self,tipo, nome, idade, cpf, fone, curso, salario):
        super().__init__(tipo, nome, idade, cpf, fone)
        self.curso = curso
        self.salario = salario
        self.tipo = tipo


    #def __del__(self):
    #    del self.curso
    #    del self.salario
    #   del self.tipo
        
        #print("Matricula Encerrada")
             
    def get_curso(self):
        return self.curso    
    def set_curso(self,curso):
        self.curso.curso = curso    
            
    
    def get_salario(self):
        return self.salario    
    def set_salario(self,salario):
        self.salario = salario

    def get_tipo(self):
        return self.tipo    
    def set_tipo(self,tipo):
        self.tipo = tipo 


    def get_desconto(self):
        return 0
    def set_desconto(self,desconto):
        print(f' Aluno não elegível ao desconto')
    
    def __str__(self):
        super().__str__()
        print(f"salario: {self.salario}")
        print(f"curso: {self.curso}")
        
        