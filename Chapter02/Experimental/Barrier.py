#%%barrier = 3 thread akan nge print dalam waktu yang beda, tapi pas wait->bakal print bareng
# barrier akan menunggu thread lain untuk beres execute 

from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

num_mhs = 3 #jumlah thread
b = Barrier(num_mhs) 
mhs = ['Ahmad', 'Alwi', 'Abdul']

def runner():
    name = mhs.pop()
    sleep(randrange(2, 10))
    print('%s Berangkat kuliah pada: %s ' % (name, ctime()))
    b.wait() # digunakan untuk block semua thread
    print('%s Pulang kuliah pada: %s ' % (name, ctime()))

def main():
    threads = []
    print('Gas kuliah!!!!')
    for i in range(num_mhs):
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()
    print('Udah pada balik!')

if __name__ == "__main__":
    main()

#%%barrier = 3 thread akan nge print dalam waktu yang beda, tapi pas wait->bakal print bareng
# barrier akan menunggu thread lain untuk beres execute 

import time
import random
import threading

def f(b):
    time.sleep(random.randint(2, 10)) #
    print("{} execute ketika: {}".format(threading.current_thread().getName(), time.ctime()))
    b.wait() # digunakan untuk block semua thread
    print("{} keluar dari: {}".format(threading.current_thread().getName(), time.ctime()))

barrier = threading.Barrier(3)
for i in range(3):
    t = threading.Thread(target=f, args=(barrier,))
    t.start()

# %%
