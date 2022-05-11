#Spawn a Process – Chapter 3: Process Based Parallelism

# membuat sebuah child process dari sebuah parent process
import multiprocessing

def fungsiKu(i): 
    print ('memberi rekomendasi alamat kost dengan nomor: %s' %i)
    for j in range (0,i):
        print('serta ruangan berjumlah berjumlah :%s' %j)
    return

if __name__ == '__main__': 
    for i in range(6):
        process = multiprocessing.Process(target=fungsiKu, args=(i,))
        process.start()
        process.join()