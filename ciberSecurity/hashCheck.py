# Descrição
# Criar um sistema simples que verifica a integridade de arquivos, comparando o hash fornecido pelo usuário com o hash real do arquivo. Na função verificar_hashes que irá receber uma lista de hashes e compará-los com os valores esperados para cada arquivo. Seu objetivo é verificar se o hash calculado é igual ao hash esperado.

# Entrada
# Uma lista de pares de hashes (hash calculado e hash esperado), separados por vírgulas, e cada par separado por ponto e vírgula.

# Saída
# Para cada par de hashes fornecido, o código imprime o resultado "Correto" ou "Inválido".

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	                       Saída
# abc123, abc123	              Correto
# def456, def789	              Inválido
# 123abc, 123abc; 456def,456def	  Correto
#                                 Correto


def verificar_hashes(lista_hashes):

    for hash_comparacao in lista_hashes:

        hash_calculado, hash_esperado = hash_comparacao.split(",")

        # TODO: Verifique se o hash calculado é igual ao hash esperado:
        if hash_calculado == hash_esperado:
            print("Correto")
        else:
            print("Inválido")


def main():
    hashes_usuario = input(
        "Digite os pares de hash calculado e hash esperado separados por vírgulas, e cada par de hashes separados por ponto e vírgula (abc123,abc123;def456,ghi789): "
    )
    hashes_usuario = hashes_usuario.replace(
        " ", ""
    )  # .replace(" ", "") está utilizando o método replace da classe str (string) para remover todos os espaços em branco de uma string. O método replace recebe dois argumentos: o primeiro é o caractere que será substituído e o segundo é o caractere que substituirá o primeiro. Neste caso, estamos substituindo todos os espaços em branco por uma string vazia, ou seja, estamos removendo todos os espaços em branco da string.

    lista_hashes = hashes_usuario.split(";")

    verificar_hashes(lista_hashes)


if __name__ == "__main__":
    main()
