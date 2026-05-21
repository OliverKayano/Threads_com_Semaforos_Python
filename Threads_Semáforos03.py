# 3. Fazer uma aplicação de uma corrida de sapos, com 5 Threads, cada Thread controlando 1
# sapo. Deve haver um tamanho máximo para cada pulo do sapo (em centímetros) e a distância
# máxima para que os sapos percorram. A cada salto, um sapo pode dar um salto de 0 até o
# tamanho máximo do salto (valor aleatório entre 1 e 5 cm.). Após dar um salto, a Thread, para
# cada sapo, deve mostrar no console, qual foi o tamanho do salto e quanto o sapo percorreu.
# Assim que o sapo percorrer a distância máxima, a Thread deve apresentar a posição que
# o sapo chegou.

import multiprocessing as mp
import random

chegada: int = 0
semaforo = None

def init(cheg, s):
    global semaforo
    global chegada 
    chegada = cheg
    semaforo = s

def corrida(id, distancia):
    max: int = 0
    dist_percorrida: int = 0
    max = random.randint(1, 5)

    while (distancia > dist_percorrida):
        salto = random.randint(0, max)
        dist_percorrida += salto
        print("\n"+f"Sapo #{id} - salto: {salto}, distância percorrida: {dist_percorrida}")
    
    with semaforo:
        chegada.value += 1
        print("\n"+f"O sapo #{id} chegou em {chegada.value}o.")


def main():
    sem = None
    chegada: int = 0
    chegada = mp.Value('i', 0)
    distancia: int = 0
    distancia = int(input("Insira a distância do percurso em cm: "))

    id: int = 0
    sapo: int = []

    for id in range(0, 5):
        sapo.append([id, distancia])
    with mp.Manager() as manager:
        sem = manager.Semaphore(1)
        with mp.Pool(processes=5, initializer=init, initargs=(chegada, sem)) as pool:
            pool.starmap(corrida, sapo)

if __name__ == '__main__':
    main()