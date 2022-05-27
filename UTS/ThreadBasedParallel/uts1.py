from random import randrange
import threading
from time import ctime, sleep
from threading import Barrier, Thread

data = 3
barrier = Barrier(data)
topic = ['Recomendation', 'Prediction', 'Diagnose']

def Dat(thread_number):
    name = topic.pop()
    sleep(randrange(1, 11))
    print('{}topik dikerjakan pada: {}'.format(name, ctime()))
    barrier.wait()
    print('{}dikumpulkan pada: {}dan selesai ke  {}' .format(name, ctime(), thread_number))
    # print('Dia adalah mahasiswa yang keluar ke N°{}'.format(thread_number))

def topik(jmlh=None):
    print("Jumlah  yang topik ada pada hari {} adalah {} topik".format(ctime(), jmlh))


def main():
    th = []
    print('Dimulai')
    for i in range(data):
        th.append(Thread(target=Dat, name="Dat", args=(i,), group=None, kwargs=None))
        th[-1].start()
    for j in th:
        j.join()
    print('Selesai')


dict = {'jmlh': data}

th1 = threading.Thread(target=topik, name="topik", group=None, kwargs=dict)

th1.start()

th1.join()


if __name__ == "__main__":
    main()




