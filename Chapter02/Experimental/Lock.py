#%%  dengan lock
import threading
import time

konci = threading.Lock()

def orang_pertama(konci):
    konci.acquire()
    print('orang - 1 sedang menggunakan kamar mandi')
    time.sleep(1)
    print('orang - 1 sudah selesai')
    konci.release()

def orang_kedua(konci):
    konci.acquire()
    print('orang - 2 sedang menggunakan kamar mandi')
    time.sleep(1)
    print('orang - 2 sudah selesai')
    konci.release()

t1 = threading.Thread(target=orang_pertama, args=(konci, ))
t2 = threading.Thread(target=orang_kedua, args=(konci, ))

t1.start()
t2.start()

t1.join()
t2.join()

#%% tanpa lock
import threading
import time

# konci = threading.Lock()

def orang_pertama():
    # konci.acquire()
    print('orang - 1 sedang menggunakan kamar mandi')
    time.sleep(1)
    print('orang - 1 sudah selesai')
    # konci.release()

def orang_kedua():
    # konci.acquire()
    print('orang - 2 sedang menggunakan kamar mandi')
    time.sleep(1)
    print('orang - 2 sudah selesai')
    # konci.release()

t1 = threading.Thread(target=orang_pertama)
t2 = threading.Thread(target=orang_kedua)

t1.start()
t2.start()

t1.join()
t2.join()
# %%
