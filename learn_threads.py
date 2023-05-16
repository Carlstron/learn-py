from time import sleep
from threading import Thread
from threading import Lock

# class MeuThread(Thread):
#     def __init__(self, text, time):
#         self.text = text
#         self.time = time
#         super().__init__()

#     def run(self):
#         sleep(self.time)
#         print(self.text)


# t1 = MeuThread('Thread 1', 5)
# t1.start()
# t2 = MeuThread('Thread 2', 7)
# t2.start()
# t3 = MeuThread('Thread 3', 2)
# t3.start()


# for i in range(20):
#     print(i)
#     sleep(1)
"""
def demorar(text, time):
    sleep(time)
    print(text)


t = Thread(target=demorar, args=('Salve', 5))
t.start()

for i in range(10):
    sleep(.5)
    print(i)
"""

"""
def demorar(text, time):
    sleep(time)
    print(text)


t = Thread(target=demorar, args=('Salve', 5))
t.start()

while t.is_alive():
    print('Esperando a Thread')
    sleep(2)
"""


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, qtd):
        self.lock.acquire()
        if self.estoque < qtd:
            print('não temos ingressos')
            self.lock.release()
            return
        sleep(1)
        self.estoque -= qtd
        print(f'Você comprou {qtd} ingressos. ainda temos {self.estoque}')
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
