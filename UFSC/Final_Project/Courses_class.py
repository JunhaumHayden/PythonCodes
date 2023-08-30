class Courses():
      
    def __init__(self,curso,valor):
        self.curso = curso
        self.valor = valor
        
    def get_curso(self):
        return curso
    def set_addCurso(self,curso):
        self.curso = curso
    def set_addValor(self,valor):
        self.valor = valor
    
    def set_removeCurso(self,curso):
        del dict_curso[curso]    
    
    def __str__(self):
        print(f" \nTipo: {self.curso} \nNome: {self.valor}")
