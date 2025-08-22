class Courses():
      
    def __init__(self,curso, valor, nota01, nota02):
        self.curso = curso
        self.valor = valor
        self.nota01 = nota01 
        self.nota02 = nota02
        
    def get_curso(self):
        return self.curso
    def set_curso(self,curso):
        self.curso = curso

    def get_valor(self):
        return self.valor    
    def set_valor(self,valor):
        self.valor = valor
    
    def set_removeCurso(self,curso):
        del dict_curso[curso]  

    def get_nota01(self):
        return self.nota01
    def set_nota01(self,valor):
        self.nota01 = valor

    def get_nota02(self):
        return self.nota02
    def set_nota02(self,valor):
        self.nota02 = valor  
    
    def __str__(self):
        print(f" \ncurso: {self.curso} \nvalor: {self.valor} \nNnota01: {self.nota01} \nnota02: {self.nota02}")
