#Exercício 1: Implemente a classe Funcionario e a classe Gerente.
# Crie a classe Assistente, que também é um funcionário, e que possui um número de matrícula (faça o método GET). Sobrescreva o método exibeDados().
# Sabendo que os Assistentes Técnicos possuem um bônus salarial e que os Assistentes Administrativos possuem um turno (dia ou noite) e um adicional noturno, crie as classes Tecnico e Administrativo.

class Funcionario:
    def __init__(self, tipo, nome, salario):
        self.tipo = tipo
        self.nome = nome
        #self.cpf = cpf
        self.salario = salario

    def __str__(self):
        print(f"\nFunção: {self.tipo} \nNome: {self.nome} \nsalario: {self.salario} ")
    
    def exibeDados(self):
        print("FUNÇãO:", self.tipo)
        print("NOME:", self.nome)
        #print("CPF:", self.cpf)
        print("SALARIO:", self.salario)


class Gerente(Funcionario):
    def __init__(self, tipo, nome, salario, bonus):
        super().__init__(tipo, nome, salario)
        self.bonus = bonus
        self.tipo = tipo

    def __str__(self):
        super().__str__()
        print(f"Bonus: {self.bonus}")

    def exibeDados(self):
        super().exibeDados()
        print("BONUS:", self.bonus)
        

class Assistente(Funcionario):
    def __init__(self, tipo, nome, salario, matricula):
        super().__init__(tipo, nome, salario)
        self.matricula = matricula
    
    def getMatricula(self):
        return self.matricula
    
    def exibeDados(self):
        super().exibeDados()
        print("MATRICULA:", self.matricula)


class Tecnico(Assistente):
    def __init__(self, tipo,  nome, salario, matricula, bonus):
        super().__init__(tipo, nome, salario, matricula)
        self.bonus = bonus
    
    def exibeDados(self):
        super().exibeDados()
        print("BONUS:", self.bonus)


class Administrativo(Assistente):
    def __init__(self, tipo, nome, salario, matricula, turno, adicional_noturno):
        super().__init__(tipo, nome, salario, matricula)
        self.turno = turno
        self.adicional_noturno = adicional_noturno
    
    def exibeDados(self):
        super().exibeDados()
        print("Turno:", self.turno)
        print("Adicional Noturno:", self.adicional_noturno)


# Exemplo de uso
gerente = Gerente("Gerente", "João", 5000, 1000)
gerente.exibeDados()

tecnico = Tecnico("Tecnico", "Maria", 3000, "123", 500)
tecnico.exibeDados()

admin = Administrativo("adm", "Lucas", 2500, "456", "dia", 100)
admin.exibeDados()
