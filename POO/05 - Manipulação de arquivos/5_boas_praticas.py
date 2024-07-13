from pathlib import Path

ROOT_PATH = Path(__file__).parent

# tecnica para garantir que o arquivo seja sempre fechado e lance uma excessao em caso do arquivo nao existir
try:
    with open(ROOT_PATH / "1lorem.txt", "r") as arquivo: # tecnica para sempre fechar o arquivo
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")


# try:
#     with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
#         arquivo.write("Aprendendo a manipular arquivos utilizando Python.")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo {exc}")

try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")
except UnicodeDecodeError as exc:
    print(exc)
