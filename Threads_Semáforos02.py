#2. Quatro pessoas caminham, cada uma em um corredor diferente. Os 4 corredores terminam
#em uma única porta. Apenas 1 pessoa pode cruzar a porta, por vez. Considere que cada
#corredor tem 200m. e cada pessoa anda de 4 a 6 m/s. Cada pessoa leva de 1 a 2 segundos
#para abrir e cruzar a porta. Faça uma aplicação que simule essa situação.

import random
import multiprocessing as mp
import time

porta: int = []
semaforo = None
passa: int = []
semaforo_passa = None

def init(cheg, p, s, sp):
    global porta
    global semaforo
    global passa
    global semaforo_passa
    passa = p
    porta = cheg
    semaforo = s
    semaforo_passa = sp

def ordem(vel, m, id):
    global porta
    dist: int = 0
    while (dist <= m):
        dist += vel

    with semaforo:
        chegada(id)

    with semaforo_passa:
        passa.value += 1
        passando(id)

def chegada(id):
    global porta
    global passa
    global semaforo_passa
    porta.value += 1
    print ('\n'+f"Pessoa do corredor {id} foi a {porta.value}o. a chegar na porta")

def passando(id):
    global passa
    tempo: int = 0
    tempo = random.randint(1,2)

    time.sleep(tempo)
    print (f"{passa.value}a. pessoa passou pela porta (corredor n.{id})")


def main():
    chegada: int = 0
    sem = None
    sem2 = None
    corredor: int = 0
    corredor = 200
    velocidade: int = 0
    params = []
    chegada = mp.Value('i', 0)
    passa = mp.Value('i', 0)

    id = ['1', '2', '3', '4']
    random.shuffle(id)

    for i in range (0, 4):
        velocidade = random.randint(4, 6)
        params.append([velocidade, corredor, id[i]])
    
    with mp.Manager() as manager:
        sem = manager.Semaphore(1)
        sem2 = manager.Semaphore(1)
        with mp.Pool(processes=4, initializer=init, initargs=(chegada, passa, sem, sem2)) as pool:
            pool.starmap(ordem, params)

if __name__=='__main__':
    main()