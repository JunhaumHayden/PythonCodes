import random
import uuid
from datetime import datetime

def gerar_numero():
    data_formatada = datetime.now().strftime("%Y%m%d_%H%M")
    numero_aleatorio = str(random.randint(10, 99))
    identificador_unico = str(uuid.uuid4().hex)[:2]  # Dois primeiros dígitos do UUID
    numero_gerado = f"{data_formatada}_{numero_aleatorio}{identificador_unico}"
    return numero_gerado

minha_string = (gerar_numero()[-4:])

# Selecionando os 4 últimos caracteres
ultimos_quatro = minha_string[-4:]
print(minha_string)
print(ultimos_quatro)
