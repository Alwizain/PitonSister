from do_something import *
import time
import threading

if __name__ == "__main__":
    start_time = time.time()
    size = 1000
    threads = 2  
    jobs = []
    for i in range(0, threads):
        out_list = list()
        thread = threading.Thread(target=do_something(size, out_list))
        jobs.append(thread)
    for j in jobs:
        j.start()

    
    for j in jobs:
        j.join()

    print ("List processing complete.")
    end_time = time.time()
    print("multithreading time=", end_time - start_time)
	
#%% studi kasus
# def sarapan():
#     time.sleep(3)
#     print('sia keur sarapan')

# def ngopi():
#     time.sleep(4)
#     print('sia keur ngopi')

# def study():
#     time.sleep(5)
#     print('sia keur diajar')

# #berapa lama si 3 function bisa selesai
# # ini main thread
# sarapan()
# ngopi()
# study()

# print(threading.active_count())
# print(threading.enumerate())