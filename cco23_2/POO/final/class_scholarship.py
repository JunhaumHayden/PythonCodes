from class_student import Students


class Scholarship(Students):
    """Classe de estudantes Bolsistas"""
    def __init__(self, tipo, nome, idade, cpf, fone, nome_resp, curso, mensalidade, desconto):
        super().__init__(tipo, nome, idade, cpf, fone, nome_resp, curso, mensalidade)
        self.desconto = desconto

    #def __del__(self):
    #    del self.desconto
        
        #print("Matricula Encerrada")
        

    def get_desconto(self):
        return self.desconto
    def set_desconto(self, desconto):
        self.desconto = desconto


    def get_mensalidade(self):
        return (self.valor - ((self.valor * self.desconto) / 100))
    def set_mensalidade(self,mensalidade):
        self.curso.valor = mensalidade

    def get_curso(self):
        return self.curso.curso    
    def set_curso(self,curso):
        self.curso.curso = curso 

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
        

    def __str__(self):
        super().__str__()
        print(f"desconto: {self.desconto}")

    def get_informacoes(self):
        print('-' * 30)
        print("desconto:", self.desconto)
        print( )
        print( )
    

        