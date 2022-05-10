from do_something import *
import time
import multiprocessing


if __name__ == "__main__":
    start_time = time.time()
    size = 10000000   
    procs = 1   #berapa kali hitung nya
    jobs = []
    for i in range(0, procs):
        out_list = list()
        process = multiprocessing.Process\
                  (target=do_something,args=(size,out_list))
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print ("List processing complete.")
    end_time = time.time()
    print("multiprocesses time=", end_time - start_time)


#%%

# from multiprocessing.dummy import Process

# #menghitung berapa kalo ngitung dari 0 ke sejuta

# def counter(num):
#      count = 0
#      while count < num:
#          count += 1

# def main():

#     a = Process(target=counter, args=(100,))
#     a.start()

#     a.join()

#     print('asdads',time.perf_counter(),'detik')

# if __name__ == "__main__":
#     main()