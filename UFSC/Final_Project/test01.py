#courses class.py
dict_curso = {'Matemática':150,'Português':100,'Literatura':120}
list = list()

list.append(Course(
class Courses():
    dict_curso = {'Matemática':150,'Português':100,'Literatura':120}
    
    def __init__(self,curso,valor):
        self.curso = curso
        self.valor = valor
        
    def get_curso(self):
        return curso
    def set_addCurso(self,curso):
        #self.dict_curso[curso] = valor
        self.curso = curso
    def set_addValor(self,valor):
        #self.dict_curso[curso] = valor
        self.valor = valor
    
    def set_removeCurso(self,curso):
        del dict_curso[curso]    
    
    def __str__(self):
        print(f" \nTipo: {self.curso} \nNome: {self.valor}")

list.append(Courses('ciencias', 200))
list.append(Courses('Matemática':150))
list.append(Courses('Português':100))
        
    