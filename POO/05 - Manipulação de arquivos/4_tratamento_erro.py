from pathlib import Path

ROOT_PATH = Path(__file__).parent


try:
    arquivo = open(ROOT_PATH / "novo-diretorio" / "novo.txt", "r")
except FileNotFoundError as exc: # Excessao de arquivo nao encontrado, "as exc" usado para capturar o detalhe da excessao
    print("Arquivo não encontrado!")
    print(exc)
except IsADirectoryError as exc: # excessao quando se tentar abrir um diretorio como arquivo
    print(f"Não foi possível abrir o arquivo: {exc}")
except IOError as exc: # IOError erro de entrada e saida, como estouro de memoria
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc: # Exception usado para qualquer outro erro
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")


# try:
#     arquivo = open(ROOT_PATH / "novo-diretorio")
# except IsADirectoryError as exc:
#     print(f"Não foi possível abrir o arquivo: {exc}")
