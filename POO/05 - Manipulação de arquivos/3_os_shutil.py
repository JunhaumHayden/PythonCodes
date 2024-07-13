import os
import shutil
from pathlib import Path #pathlib modulo para identificar diretorios

ROOT_PATH = Path(__file__).parent # __file__ funcao do python para mapear diretorios. Instanciado o caminho do diretorio na classe Path pode-se utilizar os metodos da classe, como por exemplo, .parent()

print(ROOT_PATH) #obtendo o caminho de forma dinamica (em tempo de execuçao) do diretorio

os.mkdir(ROOT_PATH / "novo-diretorio") # Para usar o caminho dinamico usa-se o divisor / que é universal para todos os SO e o "Nome_do_Diretorio"

arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

os.remove(ROOT_PATH / "alterado.txt")

shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")
