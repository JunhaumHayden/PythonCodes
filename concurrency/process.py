import multiprocessing
from time import sleep

def minha_funcao():

    while True:
        print(f"Executando...")

import multiprocessing
def worker():
    print("Processo em execução")



if __name__ == '__main__':
    proc = multiprocessing.Process(target=minha_funcao)
    proc.start()
    # Finaliza o processo após algum tempo
    sleep(2)  # Aguarda 5 segundos
    print("Finalizando o processo...")
    # Finaliza o processo
    proc.terminate()  # Força o encerramento

    p = multiprocessing.Process(target=worker)
    p.start()
    print("PID do processo:", p.pid)  # Exibe o ID do processo
    p.join()
    p = multiprocessing.Process(target=worker, name="MeuProcesso")
    print("Nome do processo:", p.name)  # Saída: "MeuProcesso"
