import threading
import time
import random

fila =30
tempo = 0
semaforo = threading.Semaphore(1)


def avancar():
    semaforo.acquire()
    global fila
    global tempo
    fila = fila - 1
    print(threading.currentThread().getName())
    time.sleep(random.randint(3,10))
    semaforo.release()

if __name__=="__main__":
    while fila > 0:
        t1 = threading.Thread(target=avancar)
        t2 = threading.Thread(target=avancar)
        t3 = threading.Thread(target=avancar)
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()
    print("\nSem clientes...\n")    