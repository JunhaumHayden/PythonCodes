from datetime import date, datetime, timedelta # timedelta para realizar operacoes, datetime modulo que opera data e hora, data é o modulo que opera apenas com dia

# Exemplo de lavacao - Dividido por categortia. Cada categoria terá um intervalo de tempo para a lavagem

tipo_carro = "M"  # P, M, G
# variaveis com escaleres
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
#
data_atual = datetime.now() # funcao para construir data hora com time zone, datetime.today() data hora de hoje, 

# condicao para selecionar a categoria
if tipo_carro == "P":
    data_estimada = data_atual - timedelta(days=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual - timedelta(days=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual - timedelta(days=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")

# operando com dias
print(date.today() - timedelta(days=1))


# operando apenas com a hora
# timedelta não opera apenas com a hora, mas sim com data e hora. Necessario operar com um objeto datetime
# No modulo datetime precisa passar uma data hora completa arbitraria para que seja possivel operar apenas a hora
resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
# apos operar exibir o resultado com a funcao .time() que retorna apenas a hora
print(resultado.time())
# Para operar apenas com dia usar a funcao .date()
print(datetime.now().date())
