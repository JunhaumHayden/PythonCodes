from PlanoDeTreino import PlanoDeTreino
from usuario import Usuario


def main():
    # Solicitar informações do usuário
    # biotipo = input("Informe o seu biotipo (Ectomorfo, Mesomorfo, Endomorfo): ")
    # dias_treino = int(input("Quantos dias por semana você tem disponível para treinar? (1, 3 ou 5): "))
    # tipo_exercicio = input("Qual o tipo de exercício preferido (Funcional, Maquinário, Peso Livre, Cardio, HIIT): ")

    # # Criar objeto Usuario
    # usuario = Usuario(biotipo, dias_treino, tipo_exercicio)
    usuario = Usuario("Ectomorfo", 3, "Livre")

    # Criar e gerar o plano de treino personalizado
    plano = PlanoDeTreino(usuario)
    plano.gerar_plano()


if __name__ == "__main__":
    main()
