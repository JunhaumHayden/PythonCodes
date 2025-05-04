from datetime import date, datetime, time
print("Exemplo de data")
data = date(2023, 7, 10)
print(data)
print("Exemplo de data com o método today()")
print(date.today())


data_hora = datetime(2023, 7, 10)
print("Exemplo de data e hora")
print(data_hora)
print("Exemplo de data e hora com o método today()")
print(datetime.today())

print("Exemplo de data e hora com o método now()")
data_hora = datetime.now()
print("Exemplo de hora")
hora = time(10, 20, 0)
print(hora)
