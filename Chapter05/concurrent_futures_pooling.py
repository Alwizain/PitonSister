import concurrent.futures
import time


time.clock = time.time
number_list = list(range(1, 11))


def hitung(number):
    for i in range(10000000):
        i += 1
    return i*number


def hasil(barang):
    result_barang = hitung(barang)
    print('Jika %s maka harganya %s' % (barang, result_barang))

if __name__ == '__main__':
    # Sequential Execution
    start_time = time.clock()
    for i in number_list:
        hasil(i)
    print('Sequential Execution = %s seconds' % (time.clock() - start_time))
    print("")

   
    # Thread Pool Execution
    start_time = time.clock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for i in number_list:
            executor.submit(hasil, i)
    print('Thread Pool Execution = %s seconds' % (time.clock() - start_time))
    print("")

      
    # Process Pool Execution
    start_time = time.clock()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for i in number_list:
            executor.submit(hasil, i)
    print('Process Pool Execu1tion = %s seconds' % (time.clock() - start_time))
