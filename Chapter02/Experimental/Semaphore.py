
#%%
import threading
import time

semaphore = threading.Semaphore(2)

def test():
    semaphore.acquire()    
    time.sleep(1)   
    print("{} : {}".format(threading.current_thread().getName(), time.ctime())) 
    semaphore.release()  


if __name__ == "__main__":

    thread_list= list()
    for i in range(20):
        t=threading.Thread(target=test,args=())
        thread_list.append(t)
        t.start()  

    for t in thread_list:
        t.join()

    print("Selesai")

# %%
