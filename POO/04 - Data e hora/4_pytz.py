from datetime import datetime
# pip install pytz
# pytz é uma biblioteca que permite trabalhar com timezones
import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)
