import multiprocessing
from multiprocessing import Barrier, Lock, Process
from random import randrange
from time import sleep, time
from datetime import datetime


def denganBarrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    sleep(randrange(1, 11))
    synchronizer.wait()
    now = time()
    with serializer:
        print("process %s = %s" %(name,datetime.fromtimestamp(now)))

def tanpaBarrier():
    name = multiprocessing.current_process().name
    sleep(randrange(1, 11))
    now = time()
    print("process %s = %s" %(name ,datetime.fromtimestamp(now)))

if __name__ == '__main__':
    synchronizer = Barrier(2)
    serializer = Lock()
    Process(name='p1 - denganBarrier', target=denganBarrier, args=(synchronizer,serializer)).start()
    Process(name='p2 - denganBarrier' ,target=denganBarrier, args=(synchronizer,serializer)).start()
    Process(name='p3 - tanpaBarrier' ,target=tanpaBarrier).start()
    Process(name='p4 - tanpaBarrier' ,target=tanpaBarrier).start()
    
