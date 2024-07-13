# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.

import re

# import requests

# response = requests.get('https://httpbin.org/ip')

# print('Your IP is {0}'.format(response.json()['origin']))


def validate_numero_telefone(phone_number):
    pattern = r"^\(\d{2}\) 9\d{4}-\d{4}$"
    if re.match(pattern, phone_number):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."


phone_number = input("Insira o número de telefone: ")
# result = validate_numero_telefone(phone_number)
print(validate_numero_telefone(phone_number))
