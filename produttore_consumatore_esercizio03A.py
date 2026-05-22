import threading
import random

DIM_BUFFER = 5
N_PRODUTTORI = 3
N_CONSUMATORI = 2
N_ORDINI = 6

buffer = [None] * DIM_BUFFER
metti = 0
togli = 0

vuoto = threading.Semaphore(DIM_BUFFER)
pieno = threading.Semaphore(0)
mutexP = threading.Semaphore(1)
mutexC = threading.Semaphore(1)


def genera_ordine():
    return f"ORD-{random.randint(10000, 99999)}"


class ProduttoreThread(threading.Thread):
    def __init__(self, idx):
        super().__init__()
        self.idx = idx

 def run(self)
    global metti
    for _ in range(6):
      self.dato=genera_ordine()
      self vuoto.acquire()
      self mutexP.acquire()
      i_metti(metti)
      metti=(metti+1)%DIM_BUFFER
      mutexP.release()
 
    buffer[i_metti]= genera_ordine()
    print(f"[SHOP_N] creato ordine{self.dato})
    



    # DA IMPLEMENTARE (run)
 class ConsumatoreThread(threading.Thread):
    def __init__(self, idx):
     super().__init__()
     self.idx = idx

    def run(self):
     global togli

     while True 
     pieno.acquire()
     mutexC.acquire()
     i_togli=togli
     togli=(togli+1)%DIM_BUFFER
     mutexC.release()
     dato=buffer[i_togli]

     if dato is None
     break

print(f"[PACK_N]prepara{self.dato})


    # DA IMPLEMENTARE (run)
    def main():
    global metti

    produttori = [ProduttoreThread(i + 1) for i in range(3)]
    consumatori = [ConsumatoreThread(i + 1) for i in range(2)]

    # DA IMPLEMENTARE: start dei thread produttori e consumatori
    for P in ProduttoreThread:
    P.start()

    for C in ConsumatoreThread:
    C.start()
    # DA IMPLEMENTARE: join di tutti i produttori
    for P in ProduttoreThread:
    P.join()

    print("Tutti i canali hanno terminato. Chiusura addetti...")

    # Invia un messaggio None per ogni addetto.
    for _ in range(3):
        # DA IMPLEMENTARE: inserire None nel buffer
        buffer=none
        pass

    # DA IMPLEMENTARE: join di tutti i consumatori
    for C in ConsumatoreThreadThread:
    C.join()

    print("Magazzino chiuso.")


if __name__ == "__main__":
    main()











