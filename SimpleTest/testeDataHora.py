import datetime

# Obtenha a data atual no UTC usando o método recomendado
data_atual = datetime.datetime.now(datetime.timezone.utc).date()
data = datetime.datetime.now(datetime.timezone.utc).strftime("%d-%m-%Y %H:%M:%S")

# Imprima a data atual
print(f"A data atual em UTC é: {data_atual}")
print(f"A data atual em UTC formatada é: {data}")

