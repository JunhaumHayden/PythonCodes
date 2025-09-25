from time import sleep
from random import randint
from threading import Thread, Semaphore

def produtor(s_vaga, s_item):
  global buffer
  for i in range(10):
    sleep(randint(0,2))           # fica um tempo produzindo...
    item = 'item ' + str(i)
    # verifica se há lugar no buffer
    s_vaga.acquire()           # aguarda que haja lugar no buffer
    buffer.append(item)
    print('Produzido %s (ha %i itens no buffer)' % (item,len(buffer)))
    s_item.release()  # sinaliza que há um item no buffer

def consumidor(s_vaga, s_item):
  global buffer
  for i in range(10):
    # aguarda que haja um item para consumir
    s_item.acquire()  # aguarda que haja um item no buffer
    item = buffer.pop(0)
    print('Consumido %s (ha %i itens no buffer)' % (item,len(buffer)))
    s_vaga.release()  # sinaliza que há um lugar no buffer
    sleep(randint(0,2))         # fica um tempo consumindo...

if __name__ == '__main__':
  buffer = []
  tam_buffer = 3
  # cria semáforos
  sem_vaga = Semaphore(tam_buffer)  # controla o número de vagas no buffer
  sem_item = Semaphore(0)            # controla o número de itens no buffer
    # cria threads
  produtor = Thread(target=produtor, args=(sem_vaga, sem_item))
  consumidor = Thread(target=consumidor, args= (sem_vaga, sem_item))
  produtor.start()
  consumidor.start()
  produtor.join()
  consumidor.join()


