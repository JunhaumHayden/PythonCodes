# Desafio
# Você está trabalhando para uma empresa que utiliza extensivamente os serviços da AWS, e após algumas análises a equipe de segurança identificou que algumas senhas dos usuários no IAM são fracas e podem representar um risco à segurança dos dados da empresa. Para resolver esse problema, foi solicitado que você desenvolva um programa capaz de analisar as senhas dos usuários e fornecer uma validação de força com base em critérios predefinidos.

# Requisitos de segurança para a senha:

# A senha deve ter no mínimo 8 caracteres.
# A senha deve conter pelo menos uma letra maiúscula (A-Z).
# A senha deve conter pelo menos uma letra minúscula (a-z).
# A senha deve conter pelo menos um número (0-9).
# A senha deve conter pelo menos um caractere especial, como !, @, #, $, %, etc.
# Entrada
# A entrada será uma única string representando a senha que precisa ser validada.

# Saída
# # Seu programa deve retornar uma mensagem indicando se a senha fornecida pelo usuário atende aos requisitos de segurança ou não, juntamente com um feedback explicativo sobre os critérios considerados.

def verificar_forca_senha(senha):
    """uma única string representando a senha que precisa ser validada"""
    comprimento_minimo = 8
    tem_letra_maiuscula = False
    tem_letra_minuscula = False
    tem_numero = False
    tem_caractere_especial = False

    # Verificando o comprimento da senha
    if len(senha) < comprimento_minimo:
        return f"Sua senha é muito curta. Recomenda-se no mínimo {comprimento_minimo} caracteres."

    # Verificando se a senha contém letras maiúsculas, minúsculas, números e caracteres especiais
    for caractere in senha:
        if caractere.isupper():
            tem_letra_maiuscula = True
        elif caractere.islower():
            tem_letra_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif not caractere.isalnum():
            tem_caractere_especial = True

    # Verificando se a senha contém sequências comuns
    sequencias_comuns = ["123456", "abcdef"]
    for sequencia in sequencias_comuns:
        if sequencia in senha:
            return "Sua senha contém uma sequência comum. Tente uma senha mais complexa."

    # Verificando se a senha contém palavras comuns
    palavras_comuns = ["password", "123456", "qwerty"]
    if senha in palavras_comuns:
        return "Sua senha é muito comum. Tente uma senha mais complexa."

    # Verificando os critérios de validação
    if not tem_letra_maiuscula:
        return "Sua senha deve conter pelo menos uma letra maiúscula."
    if not tem_letra_minuscula:
        return "Sua senha deve conter pelo menos uma letra minúscula."
    if not tem_numero:
        return "Sua senha deve conter pelo menos um número."
    if not tem_caractere_especial:
        return "Sua senha deve conter pelo menos um caractere especial."

    return "Sua senha é forte!"

if __name__ == '__main__':
    # Obtendo a senha do usuário
    senha = input("Digite a senha: ").strip()

    # Verificando a força da senha
    resultado = verificar_forca_senha(senha)

    # Imprimindo o resultado
    print(resultado)
