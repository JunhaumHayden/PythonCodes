from datetime import datetime

data_hora_atual = datetime.now() # variavel com data hora atual
data_hora_str = "2023-10-20 10:20" # variavel com uma string de data hora
mascara_ptbr = "%d/%m/%Y %a" # Mascara é o formato que se quer apresentar na saida
mascara_en = "%Y-%m-%d %H:%M"

data_hora_str02 = "20/10/2023 10:20"
mascara_ptbr02 = "%d/%m/%Y %H:%M" # Mascara é o formato que se quer apresentar na saida


# String Format Time - formata data hora na saida
print(data_hora_atual.strftime(mascara_ptbr))

#String Parse Time - converte string para datetime
data_convertida = datetime.strptime(data_hora_str, mascara_en) # 1 argumento é a string, 2 argumento é a mascara
print(data_convertida)

# Este codigo dará erro pq a string deve concordar com a mascara
#data_convertida = datetime.strptime(data_hora_str, mascara_ptbr02) # 1 argumento é a string, 2 argumento é a mascara
data_convertida02 = datetime.strptime(data_hora_str02, mascara_ptbr02) # 1 argumento é a string, 2 argumento é a mascara
print(f"data convertida datetime {data_convertida02}")
print(f"data mascarada em ptbr {data_convertida02.strftime(mascara_ptbr)}")
print(type(data_convertida))
