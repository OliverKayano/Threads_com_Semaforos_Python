#1. Fazer uma aplicação, console, que gerencie a figura abaixo:
#Para tal, usar uma variável sentido, que será alterado pela Thread que controla cada carro
#com a movimentação do carro. Quando a Thread tiver a possibilidade de ser executada, ela
#deve imprimir em console o sentido que o carro está passando. Só pode passar um carro por
#vez no cruzamento.

import multiprocessing as mp
import time
import random

carro_chega: int = 0
semaforo = None

def init(cheg, s):
    global carro_chega
    global semaforo
    carro_chega = cheg
    semaforo = s

def passagem(direcoes):
    global semaforo

    with semaforo:
        car_para(direcoes)

def car_para(direcoes):
    global carro_chega

    time.sleep(0.01)
    carro_chega.value += 1

    print(f"O {carro_chega.value}o. carro chega no sentido {direcoes} e passa")


def main():
    chegada: int = 0
    sem = None
    direcoes = []
    direcoes.append(['Leste'])
    direcoes.append(['Oeste'])
    direcoes.append(['Norte'])
    direcoes.append(['Sul'])

    chegada = mp.Value('i', 0)
    random.shuffle(direcoes)
    with mp.Manager() as manager:
        sem = manager.Semaphore(1)

        with mp.Pool(processes=len(direcoes), initializer=init, initargs=(chegada, sem)) as pool:
            pool.map(passagem, direcoes)

if __name__=='__main__':
    main()