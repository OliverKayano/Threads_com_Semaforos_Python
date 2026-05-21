#4. Você foi contratado para automatizar um treino de Fórmula 1. As regras estabelecidas pela
#direção da prova são simples:
#“No máximo 5 carros das 7 escuderias[equipes] (Cada escuderia tem 2 carros diferentes,
#portanto, 14 carros no total) presentes podem entrar na pista simultaneamente, mas apenas
#um carro de cada equipe. O segundo carro deve ficar à espera, caso um companheiro de
#equipe já esteja na pista. Cada piloto deve dar 3 voltas na pista. O tempo de cada volta deverá
#ser exibido.

import multiprocessing as mp
import random
import time

chegada_equipe: int = 0
semaforo_equipe = None

def init(cheg, s):
    global chegada
    global semaforo_equipe
    chegada = cheg
    semaforo_equipe = s

def corrida(id, pista):
    global semaforo_equipe
    global semaforo_carros
    global chegada_equipe

    with semaforo_equipe:
        chegada_equipe += 1
        entra_pista(id, pista)

def entra_pista(id, pista):  

   for carro in range (1, 3):
       começando(id, carro ,pista)     

def começando(id, carro, pista):

    vel = random.randint(58, 70) #vel media de corrida de formula 1 em m/s.
    voltas: int = 0
    dist: int = 0
    tempo: float = 0
  
    print('\n\n'+f'A equipe #{id} enviou o {carro}o. carro para a pista', end='')
   
    for i in range (1, 4):
             tempo = 0
             while dist < pista:
                dist += vel
                tempo += 1
          
             dist = 0
             voltas += 1
             print('\n'+f'Carro {carro}, equipe {id}, {voltas}a. volta, tempo: {tempo}.', end='')


def main():
    sem = None
    chegada: int = 0
    chegada = mp.Value('i', 0)
    equipes: int = []
    pista = random.randint(3600, 7000)
    for i in range (0,7):
        equipes.append([i+1, pista])

    with mp.Manager() as manager:
        sem = manager.Semaphore(5)
        sem2 = manager.Semaphore(1)
        with mp.Pool(processes=7, initializer=init, initargs=(chegada, sem)) as pool:
            pool.starmap(corrida, equipes)

if __name__ == '__main__':
    main()