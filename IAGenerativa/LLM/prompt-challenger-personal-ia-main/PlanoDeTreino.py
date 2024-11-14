# import requests
from treino import Treino


class PlanoDeTreino:
    def __init__(self, usuario):
        self.usuario = usuario

    def gerar_plano(self):
        # Determinar o tipo de treino com base nos dias disponíveis
        if self.usuario.dias_treino == 1:
            treino = Treino(
                "Full Body", "Treino que trabalha o corpo todo em uma única sessão."
            )
        elif self.usuario.dias_treino == 3:
            treino = Treino(
                "ABC",
                "Divisão do treino em três dias, cada um focado em grupos musculares diferentes.",
            )
        elif self.usuario.dias_treino == 5:
            treino = Treino(
                "ABCDE",
                "Divisão do treino em cinco dias, com foco ainda mais específico em cada grupo muscular.",
            )
        else:
            treino = Treino(
                "Personalizado",
                "Plano de treino adaptado ao número de dias não convencional.",
            )

        # Adicionar recomendação com base no biotipo
        biotipo_recomendacao = self.recomendar_com_base_no_biotipo()

        # Adicionar recomendação com base no tipo de exercício preferido
        tipo_exercicio_recomendacao = self.recomendar_tipo_exercicio()

        # Exibir o plano de treino
        print(f"Plano de Treino Personalizado para {self.usuario.biotipo}")
        print(treino)
        print(biotipo_recomendacao)
        print(tipo_exercicio_recomendacao)

    def recomendar_com_base_no_biotipo(self):
        if self.usuario.biotipo.lower() == "ectomorfo":
            return "Recomendação: Priorizar exercícios de hipertrofia com maior volume e cargas moderadas."
        elif self.usuario.biotipo.lower() == "mesomorfo":
            return "Recomendação: Pode combinar hipertrofia e força. Boa resposta a qualquer tipo de treino."
        elif self.usuario.biotipo.lower() == "endomorfo":
            return "Recomendação: Focar em exercícios de queima calórica e aeróbicos para redução de gordura."
        else:
            return (
                "Recomendação: Biotipo desconhecido. Personalize conforme necessidade."
            )

    def recomendar_tipo_exercicio(self):
        tipo_exercicio = self.usuario.tipo_exercicio.lower()
        if tipo_exercicio == "funcional":
            return "Treino Funcional: Exercícios que trabalham o corpo de maneira integrada, com foco na mobilidade e resistência."
        elif tipo_exercicio == "maquinário":
            return "Treino em Maquinário: Uso de máquinas para isolamento muscular e controle de carga."
        elif tipo_exercicio == "peso livre":
            return "Treino com Peso Livre: Exercícios com halteres, barras e anilhas para maior ativação muscular."
        elif tipo_exercicio == "cardio":
            return "Treino Cardio: Exercícios focados em melhorar a capacidade cardiovascular."
        elif tipo_exercicio == "hiit":
            return "Treino HIIT: Exercícios de alta intensidade com intervalos curtos para queima calórica rápida."
        else:
            return "Tipo de exercício desconhecido. Personalize conforme necessidade."
        # ######Solicitação à API do Gemini (Exemplo)
        # def solicitar_exercicios_gemini(usuario):
        # url = "https://api.gemini.com/exercicios"
        # params = {
        #     "biotipo": self.usuario.biotipo,
        #     "dias_treino": self.usuario.dias_treino,
        #     "preferencia": self.usuario.preferencia_exercicio,
        # }
        # headers = {"Authorization": "AIzaSyAOF_fioAmQLzEYKnaIsacResDbxEr4E0A"}
        # response = requests.get(url, params=params, headers=headers)
        # data = response.json()
        # return data
