import time
from do_something import *

if __name__ == "__main__": # buat ngejalanin fungi main
    start_time = time.time() # variable start time untuk mulai
    size = 10  #
    n_exec = 10
    for i in range(0, n_exec):
        out_list = list()
        do_something(size, out_list)
       
 
    print ("List processing complete.")
    end_time = time.time()
    print("serial time=", end_time - start_time)
