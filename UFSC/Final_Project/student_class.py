from school_class import School

class Students(School):
    """Classe de estudantes"""
    def __init__(self, tipo, nome, idade, cpf, fone, nome_resp, curso, mensalidade):
        super().__init__(tipo, nome, idade, cpf, fone)
        self.nome_resp = nome_resp
        self.curso = curso
        self.mensalidade = mensalidade
        self.tipo = tipo

        
    def getnome_resp(self):
        return self.nome_resp    
    def setnome_resp(self,nome_resp):
        self.nome_resp = nome_resp
    
        
    def get_curso(self):
        return self.curso    
    def set_curso(self,curso):
        self.curso = curso    
            
    
    def get_mensalidade(self):
        return self.mensalidade    
    def set_mensalidade(self,mensalidade):
        self.mensalidade = mensalidade

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
        print(f"mensalidade: {self.mensalidade}")
        print(f"curso: {self.curso}")
        print(f"nome_resp: {self.nome_resp}")
        
    